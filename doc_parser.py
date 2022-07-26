import os
import os.path
from docxtpl import DocxTemplate, RichText
import sys
import subprocess
import re
from databasecreate import CreateDB
from configparser import ConfigParser


# config = ConfigParser()
# config.read('setting.ini')

class CreateFile:
	def __init__(self, cont_dict):
		self.path_dir_temp = os.path.join(os.getcwd(), 'template')
		self.path_dir_order_file = os.path.join(os.getcwd(), 'OrderBDFile')
		self.exists_file(self.path_dir_temp)
		self.exists_file(self.path_dir_order_file)
		self.template = (
			(os.path.join(self.path_dir_temp, 'act_repair.docx'), cont_dict['chk_state'][0], 'act_repair'),
			(os.path.join(self.path_dir_temp, 'act_work.docx'), cont_dict['chk_state'][1], 'act_work'),
			(os.path.join(self.path_dir_temp, 'order.docx'), cont_dict['chk_state'][2], 'order'),
			(os.path.join(self.path_dir_temp, 'act_tmc.docx'), cont_dict['chk_state'][3], 'act_tmc')
		)

		for template in self.template:
			self.print_to_file(cont_dict, *template)

	def print_to_file(self, dict_text: dict, template: str, pref: int = 0, pref_name: str = ''):
		# for key in dict_text:
		# 	print(key, ' : ', dict_text[key])
		if pref:
			document = DocxTemplate(template)

			rorder = RichText()
			rdata = RichText()
			rname = RichText()
			rbrand = RichText()
			rnum = RichText()
			radr = RichText()
			rdriv = RichText()
			rphone = RichText()
			rmphone = RichText()

			radr.add(dict_text['address'], size=24)
			rdriv.add(dict_text['driver'], size=24)
			rphone.add(dict_text['phone'], size=24)
			rmphone.add(dict_text['mphone'], size=24)

			if pref_name == 'act_tmc':
				rorder.add(dict_text['order_number'], size=32, bold=True)
				rdata.add(dict_text['crdata'], size=32, bold=True)
				rname.add(dict_text['name'], size=32, bold=True)
				rbrand.add(dict_text['brand'], size=32, bold=True)
				rnum.add(dict_text['car_number'], size=32, bold=True)
			else:
				rorder.add(dict_text['order_number'], size=24, bold=True)
				rdata.add(dict_text['crdata'], size=24)
				rname.add(dict_text['name'], size=24)
				rbrand.add(dict_text['brand'], size=24)
				rnum.add(dict_text['car_number'], size=24)

			new_dict = {
				'order_number': rorder,
				'crdata': rdata,
				'name': rname,
				'brand': rbrand,
				'car_number': rnum,
				'address': radr,
				'driver': rdriv,
				'phone': rphone,
				'mphone': rmphone
			}

			document.render(new_dict)

			path = os.path.join(self.path_dir_order_file, dict_text['path_file_dir'])
			self.exists_file(path)

			path_sep = "{path}{sep}".format(path=path, sep=os.sep)
			path_file = "{path}{name}_{pref}".format(
				path=path_sep,
				name=dict_text['file_name'],
				pref=pref_name)

			document.save(path_file + '.docx')
			
			upd = CreateDB()
			upd.update_order_path(int(dict_text['order_id']), path)

			if sys.platform == 'win32':
				if pref_name == 'order':
					self.print_to_print(path_file + '.docx')
				self.print_to_print(path_file + '.docx')
			if sys.platform == 'linux':
				convert_to(path_sep, path_file + '.docx')
				self.print_to_print(path_file + '.pdf')

	@classmethod
	def print_to_print(cls, path):
		if sys.platform == 'win32':
			os.startfile(path, "print")
		if sys.platform == 'linux':
			os.system('lpr ' + path)

	@classmethod
	def exists_file(cls, path):
		if not os.path.exists(path):
			os.makedirs(path)


def convert_to(folder, source, timeout=None):
	args = [libreoffice_exec(), '--headless', '--convert-to', 'pdf', '--outdir', folder, source]

	process = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
	filename = re.search('-> (.*?) using filter', process.stdout.decode())

	if filename is None:
		raise LibreOfficeError(process.stdout.decode())
	else:
		return filename.group(1)


def libreoffice_exec():
	if sys.platform == 'darwin':
		return '/Applications/LibreOffice.app/Contents/MacOS/soffice'
	return 'libreoffice'


class LibreOfficeError(Exception):
	def __init__(self, output):
		self.output = output


if __name__ == '__main__':
	print(sys.platform)
