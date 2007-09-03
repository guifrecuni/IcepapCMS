#!/usr/bin/env python

from distutils.core import setup
import glob
import os


if os.name == 'nt': #sys.platform == 'win32':
    import py2exe
	

setup(name = "icepapms",
      version = "0.3",
      description = "Icepap Configuration Management System and Test Tool",
      author = "Josep Joan Ribas Prats",
      author_email = "jribas@cells.es",
      url = "http://www.cells.es",
      packages = ["lib_icepapcms", "ui_icepapcms", "lib_icepapcms.pyIcePAP", "lib_icepapcms.pyIcePAP.serial","ui_icepapcms.icepapdriver_widget", "ui_icepapcms.Led"],
      data_files = [('doc', glob.glob("doc/*.*")),
                    ('templates', glob.glob("templates/*.*")),
                    ],
      scripts = ["icepapcms","icepapcms.py"],
	  console = ["icepapcms.py"],
	  windows = [
        {
            "script": "icepapcms.py",
            "icon_resources": [(1, "icepapcms.ico")]
        }
      ],
      long_description = """
IcepapCfg is a configuration and test tool for the Icepap motor controller
"""          
      )    
