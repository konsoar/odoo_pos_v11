==========================
 Hardware Network Printer
==========================

Installation
============

In PosBox
---------

* Comment out line 354 in hw_escpos/controllers/main.py, i.e. replace

  ``driver.push_task('printstatus')`` 
  
  with 
  
  ``# driver.push_task('printstatus')`` 
  
  Read here how to edit files at PosBox: https://dotop-development.readthedocs.io/en/latest/admin/posbox/administrate-posbox.html#how-to-edit-dotop-source.
* add ``hw_printer_network`` module to *server wide modules*. Detailed instruction is here: https://dotop-development.readthedocs.io/en/latest/admin/posbox/administrate-posbox.html#how-to-update-dotop-command-line-options

Usage
=====

Use the module together with `Pos Network Printer <https://apps.dotop.com/apps/modules/10.0/pos_printer_network>`__
