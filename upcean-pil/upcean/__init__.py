'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2011-2013 Cool Dude 2k - http://idb.berlios.de/
    Copyright 2011-2013 Game Maker 2k - http://intdb.sourceforge.net/
    Copyright 2011-2013 Kazuki Przyborowski - https://github.com/KazukiPrzyborowski

    $FileInfo: __init__.py - Last Update: 08/10/2013 Ver. 2.4.4 RC 1 - Author: cooldude2k $
'''

from __future__ import division, absolute_import, print_function;
__version_info__ = (2, 4, 4, "RC 1");
if(__version_info__[3]!=None):
 __version__ = str(__version_info__[0])+"."+str(__version_info__[1])+"."+str(__version_info__[2])+" "+str(__version_info__[3]);
if(__version_info__[3]==None):
 __version__ = str(__version_info__[0])+"."+str(__version_info__[1])+"."+str(__version_info__[2]);
def version_info():
 global __version_info__;
 if(__version_info__[3]!=None):
  return {"major": str(__version_info__[0]), "minor": str(__version_info__[1]), "build": str(__version_info__[2]), "release": str(__version_info__[3])};
 if(__version_info__[3]==None):
  return {"major": str(__version_info__[0]), "minor": str(__version_info__[1]), "build": str(__version_info__[2]), "release": None};
import sys, re, upcean.validate, upcean.convert, upcean.getprefix, upcean.getsfname;
import upcean.ean2, upcean.ean5, upcean.upca, upcean.upce, upcean.ean13, upcean.ean8, upcean.itf, upcean.itf14, upcean.code11, upcean.code39, upcean.code93, upcean.codabar, upcean.msi;
from sys import argv;
''' Code for validating UPC/EAN by Kazuki Przyborowski '''
from upcean.validate import *;
''' Code for converting UPC/EAN by Kazuki Przyborowski '''
from upcean.convert import *;
''' Code for getting GS1 Prefix EAN-8/EAN-13/ITF-14 by Kazuki Przyborowski '''
from upcean.getprefix import *;
''' Code for getting save file name and type by Kazuki Przyborowski '''
from upcean.getsfname import *;
''' Code for making EAN-2 supplement by Kazuki Przyborowski '''
from upcean.ean2 import *;
''' Code for making EAN-5 supplement by Kazuki Przyborowski '''
from upcean.ean5 import *;
''' Code for making UPC-A by Kazuki Przyborowski '''
from upcean.upca import *;
''' Code for making UPC-E by Kazuki Przyborowski '''
from upcean.upce import *;
''' Code for making EAN-13 by Kazuki Przyborowski '''
from upcean.ean13 import *;
''' Code for making EAN-8 by Kazuki Przyborowski '''
from upcean.ean8 import *;
''' Code for making Standard 2 of 5 by Kazuki Przyborowski '''
from upcean.stf import *;
''' Code for making Interleaved 2 of 5 by Kazuki Przyborowski '''
from upcean.itf import *;
''' Code for making ITF-14 by Kazuki Przyborowski '''
from upcean.itf14 import *;
''' Code for making Code 11 by Kazuki Przyborowski '''
from upcean.code11 import *;
''' Code for making Code 39 by Kazuki Przyborowski '''
from upcean.code39 import *;
''' Code for making Code 93 by Kazuki Przyborowski '''
from upcean.code93 import *;
''' Code for making Codabar by Kazuki Przyborowski '''
from upcean.codabar import *;
''' Code for making Modified Plessey by Kazuki Przyborowski '''
from upcean.msi import *;

'''
UPC Resources and Info
http://en.wikipedia.org/wiki/Universal_Product_Code
http://en.wikipedia.org/wiki/Global_Trade_Item_Number
http://en.wikipedia.org/wiki/Barcode
http://www.ucancode.net/CPP_Library_Control_Tool/Draw-Print-encode-UPCA-barcode-UPCE-barcode-EAN13-barcode-VC-Code.htm
http://en.wikipedia.org/wiki/International_Article_Number
http://www.upcdatabase.com/docs/
http://www.accipiter.org/projects/cat.php
http://www.accipiter.org/download/kittycode.js
http://uscan.sourceforge.net/upc.txt
http://www.adams1.com/upccode.html
http://www.documentmedia.com/Media/PublicationsArticles/QuietZone.pdf
http://zxing.org/w/decode.jspx
http://code.google.com/p/zxing/
http://www.terryburton.co.uk/barcodewriter/generator/
http://en.wikipedia.org/wiki/Interleaved_2_of_5
http://www.gs1au.org/assets/documents/info/user_manuals/barcode_technical_details/ITF_14_Barcode_Structure.pdf
http://www.barcodeisland.com/
'''

'''
Shortcut Codes by Kazuki Przyborowski
'''
def create_barcode(upc,outfile="./barcode.png",resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 upc = str(upc);
 if(not re.findall("^([0-9]*[\.]?[0-9])", str(resize)) or int(resize) < 1):
  resize = 1;
 upc_pieces = None; supplement = None;
 if(re.findall("([0-9]+)([ |\|]{1})([0-9]{2})$", upc)):
  upc_pieces = re.findall("([0-9]+)([ |\|]{1})([0-9]{2})$", upc);
  upc_pieces = upc_pieces[0];
  upc = upc_pieces[0]; supplement = upc_pieces[2];
 if(re.findall("([0-9]+)([ |\|]{1})([0-9]{5})$", upc)):
  upc_pieces = re.findall("([0-9]+)([ |\|]{1})([0-9]{5})$", upc);
  upc_pieces = upc_pieces[0];
  upc = upc_pieces[0]; supplement = upc_pieces[2];
 if(len(upc)==7 or len(upc)==8):
  if(supplement==None):
   if(re.findall("^([0-1])", upc)):
    return create_upce(upc,outfile,resize,hideinfo,barheight,barcolor);
   if(re.findall("^([2-9])", upc)):
    return create_ean8(upc,outfile,resize,hideinfo,barheight,barcolor);
  if(supplement!=None):
   if(re.findall("^([0-1])", upc)):
    return create_upce(upc+" "+supplement,outfile,resize,hideinfo,barheight,barcolor);
   if(re.findall("^([2-9])", upc)):
    return create_ean8(upc+" "+supplement,outfile,resize,hideinfo,barheight,barcolor);
 if(len(upc)==2):
  return create_ean2(upc,outfile,resize,hideinfo,barheight,barcolor);
 if(len(upc)==5):
  return create_ean5(upc,outfile,resize,hideinfo,barheight,barcolor);
 if(len(upc)==11 or len(upc)==12):
  if(supplement==None):
   return create_upca(upc,outfile,resize,hideinfo,barheight,barcolor);
  if(supplement!=None):
   return create_upca(upc+" "+supplement,outfile,resize,hideinfo,barheight,barcolor);
 if(len(upc)==13): 
  if(supplement==None):
   return create_ean13(upc,outfile,resize,hideinfo,barheight,barcolor);
  if(supplement!=None):
   return create_ean13(upc+" "+supplement,outfile,resize,hideinfo,barheight,barcolor);
 if(len(upc)==14): 
  if(supplement==None):
   return create_itf14(upc,outfile,resize,hideinfo,barheight,barcolor);
  if(supplement!=None):
   return create_itf14(upc+" "+supplement,outfile,resize,hideinfo,barheight,barcolor);
 return False;
def draw_barcode(upc,resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 return create_barcode(upc,None,resize,hideinfo,barheight,barcolor);


def create_upc(upc,outfile="./upc.png",resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 upc = str(upc);
 if(not re.findall("^([0-9]*[\.]?[0-9])", str(resize)) or int(resize) < 1):
  resize = 1;
 upc_pieces = None; supplement = None;
 if(re.findall("([0-9]+)([ |\|]{1})([0-9]{2})$", upc)):
  upc_pieces = re.findall("([0-9]+)([ |\|]{1})([0-9]{2})$", upc);
  upc_pieces = upc_pieces[0];
  upc = upc_pieces[0]; supplement = upc_pieces[2];
 if(re.findall("([0-9]+)([ |\|]{1})([0-9]{5})$", upc)):
  upc_pieces = re.findall("([0-9]+)([ |\|]{1})([0-9]{5})$", upc);
  upc_pieces = upc_pieces[0];
  upc = upc_pieces[0]; supplement = upc_pieces[2];
 if(len(upc)==7 or len(upc)==8):
  if(supplement==None):
   return create_upce(upc,outfile,resize,hideinfo,barheight,barcolor);
  if(supplement!=None):
   return create_upce(upc+" "+supplement,outfile,resize,hideinfo,barheight,barcolor);
 if(len(upc)==11 or len(upc)==12):
  if(supplement==None):
   return create_upca(upc,outfile,resize,hideinfo,barheight,barcolor);
  if(supplement!=None):
   return create_upca(upc+" "+supplement,outfile,resize,hideinfo,barheight,barcolor);
 if(len(upc)==13 or len(upc)==14): 
  if(len(upc)==13): 
    upc = "0"+upc;
  if(supplement==None):
   return create_itf14(upc,outfile,resize,hideinfo,barheight,barcolor);
  if(supplement!=None):
   return create_itf14(upc+" "+supplement,outfile,resize,hideinfo,barheight,barcolor);
 return False;
def draw_upc(upc,resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 return create_upc(upc,None,resize,hideinfo,barheight,barcolor);

def create_ean(upc,outfile="./ean.png",resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 upc = str(upc);
 if(not re.findall("^([0-9]*[\.]?[0-9])", str(resize)) or int(resize) < 1):
  resize = 1;
 upc_pieces = None; supplement = None;
 if(re.findall("([0-9]+)([ |\|]{1})([0-9]{2})$", upc)):
  upc_pieces = re.findall("([0-9]+)([ |\|]{1})([0-9]{2})$", upc);
  upc_pieces = upc_pieces[0];
  upc = upc_pieces[0]; supplement = upc_pieces[2];
 if(re.findall("([0-9]+)([ |\|]{1})([0-9]{5})$", upc)):
  upc_pieces = re.findall("([0-9]+)([ |\|]{1})([0-9]{5})$", upc);
  upc_pieces = upc_pieces[0];
  upc = upc_pieces[0]; supplement = upc_pieces[2];
 if(len(upc)==2):
  return create_ean2(upc,outfile,resize,hideinfo,barheight,barcolor);
 if(len(upc)==5):
  return create_ean5(upc,outfile,resize,hideinfo,barheight,barcolor);
 if(len(upc)==7 or len(upc)==8):
  if(supplement==None):
   return create_ean8(upc,outfile,resize,hideinfo,barheight,barcolor);
  if(supplement!=None):
   return create_ean8(upc+" "+supplement,outfile,resize,hideinfo,barheight,barcolor);
 if(len(upc)==12 or len(upc)==13): 
  if(supplement==None):
   return create_ean13(upc,outfile,resize,hideinfo,barheight,barcolor);
  if(supplement!=None):
   return create_ean13(upc+" "+supplement,outfile,resize,hideinfo,barheight,barcolor);
 if(len(upc)==14): 
  if(supplement==None):
   return create_itf14(upc,outfile,resize,hideinfo,barheight,barcolor);
  if(supplement!=None):
   return create_itf14(upc+" "+supplement,outfile,resize,hideinfo,barheight,barcolor);
 return False;
def draw_ean(upc,resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 return create_ean(upc,None,resize,hideinfo,barheight,barcolor);

def create_issn13_from_issn8(upc,outfile="./issn13.png",resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 return create_ean13(convert_issn8_to_issn13(upc),outfile,resize,hideinfo,barheight,barcolor);
def draw_issn13_from_issn8(upc,resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 return create_issn13_from_issn8(upc,None,resize,hideinfo,barheight,barcolor);
def create_issn13(upc,outfile="./issn13.png",resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 return create_issn13_from_issn8(upc,outfile,resize,hideinfo,barheight,barcolor);
def draw_issn13(upc,resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 return create_issn13(upc,None,resize,hideinfo,barheight,barcolor);

def create_isbn13_from_isbn10(upc,outfile="./isbn13.png",resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 return create_ean13(convert_isbn10_to_isbn13(upc),outfile,resize,hideinfo,barheight,barcolor);
def draw_isbn13_from_isbn10(upc,resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 return create_isbn13_from_isbn10(upc,None,resize,hideinfo,barheight,barcolor);
def create_isbn13(upc,outfile="./isbn13.png",resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 return create_isbn13_from_isbn10(upc,outfile,resize,hideinfo,barheight,barcolor);
def draw_isbn13(upc,resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 return create_isbn13(upc,None,resize,hideinfo,barheight,barcolor);

def create_ismn13_from_ismn10(upc,outfile="./ismn13.png",resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 return create_ean13(convert_ismn10_to_ismn13(upc),outfile,resize,hideinfo,barheight,barcolor);
def draw_ismn13_from_ismn10(upc,resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 return create_ismn13_from_ismn10(upc,None,resize,hideinfo,barheight,barcolor);
def create_ismn13(upc,outfile="./ismn13.png",resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 return create_ismn13_from_ismn10(upc,outfile,resize,hideinfo,barheight,barcolor);
def draw_ismn13(upc,resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 return create_ismn13(upc,None,resize,hideinfo,barheight,barcolor);

def create_vw_upca(code,price,outfile="./vw-upca.png",resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 return create_upca(make_vw_upca(code, price),outfile,resize,hideinfo,barheight,barcolor);
def draw_vw_upca(code,price,resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 return create_vw_upca(code,price,None,resize,hideinfo,barheight,barcolor);
def create_vw_to_ean13(code,price,outfile="./vw-ean13.png",resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 return create_ean13(make_vw_to_ean13(code, price),outfile,resize,hideinfo,barheight,barcolor);
def draw_vw_to_ean13(code,price,resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 return create_vw_to_ean13(code,price,None,resize,hideinfo,barheight,barcolor);
def create_vw_to_itf14(code,price,outfile="./vw-itf14.png",resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 return create_itf14(make_vw_to_itf14(code, price),outfile,resize,hideinfo,barheight,barcolor);
def draw_vw_to_itf14(code,price,resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 return create_vw_to_itf14(code,price,None,resize,hideinfo,barheight,barcolor);

def create_coupon_upca(numbersystem,manufacturer,family,value,outfile="./vw-upca.png",resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 return create_upca(make_coupon_upca(numbersystem, manufacturer, family, value),outfile,resize,hideinfo,barheight,barcolor);
def draw_coupon_upca(numbersystem,manufacturer,family,value,resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 return create_coupon_upca(numbersystem,manufacturer,family,value,None,resize,hideinfo,barheight,barcolor);
def create_coupon_to_ean13(numbersystem,manufacturer,family,value,outfile="./vw-upca.png",resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 return create_ean13(make_coupon_to_ean13(numbersystem, manufacturer, family, value),outfile,resize,hideinfo,barheight,barcolor);
def draw_coupon_to_ean13(numbersystem,manufacturer,family,value,resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 return create_coupon_to_ean13(numbersystem,manufacturer,family,value,None,resize,hideinfo,barheight,barcolor);
def create_coupon_to_itf14(numbersystem,manufacturer,family,value,outfile="./vw-upca.png",resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 return create_itf14(make_coupon_to_itf14(numbersystem, manufacturer, family, value),outfile,resize,hideinfo,barheight,barcolor);
def draw_coupon_to_itf14(numbersystem,manufacturer,family,value,resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 return create_coupon_to_itf14(numbersystem,manufacturer,family,value,None,resize,hideinfo,barheight,barcolor);