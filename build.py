#!/usr/bin/python

"""
Builds a vm and puts it in ~/public with a latest.json that has its filename and md5sum
"""
import os
import subprocess
import stat

OUTPUT_DIR = 'output-virtualbox-ovf'
PUBLIC_DIR = os.path.join(os.path.expanduser('~'),  'public')
BUILD_LIST = ["vm.json", "vm-develop.json"]


def main():
	for vm in BUILD_LIST:
		build_vm(vm)
		move_to_public()
		cleanup()
	generate_checksums()

def build_vm(vm):
	subprocess.check_call("/home/frappe/bench-develop/vm/packer build {vm}".format(vm=vm), shell=True)

def move_to_public():
	for file in get_output_files():
		dest = os.path.join(PUBLIC_DIR, file)
		file = os.path.join(OUTPUT_DIR, file)
		os.rename(file, dest)
		st = os.stat(dest)
		os.chmod(dest, st.st_mode | stat.S_IROTH)

def generate_checksums():
	for file in os.listdir(PUBLIC_DIR):
		if 'md5' not in file:
			file = os.path.join(PUBLIC_DIR, file)
			md5 = subprocess.check_output("md5sum {}".format(file), shell=True).split()[0]
			f = open(file + '.md5', 'w')
			f.write(md5)
			f.close()

def get_output_files():
	return os.listdir(OUTPUT_DIR)

def cleanup():
	os.rmdir(OUTPUT_DIR)

if __name__ == "__main__":
	main()
