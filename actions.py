# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from googletrans import Translator  
from datetime import datetime       

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pymysql
import requests, os


translator = Translator()                  


class ActionDaftarJadwal(Action):

	def name(self) -> Text:
		return "action_daftar_jadwal"

	def run(self, dispatcher: CollectingDispatcher,
	tracker: Tracker,
	domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		conn = pymysql.connect(host=os.environ.get('MYSQL_HOST'),user='root',database='chatbot_uii',port=3306,connect_timeout=5)
		mycursor = conn.cursor()

		konsentrasi = tracker.get_slot("konsentrasi")

		konsentrasi = konsentrasi.upper()

		if konsentrasi == "DATA SAINS" or konsentrasi == "SAINS DATA":
			konsentrasi = "DATA SCIENCE"
		
		# message = '''semester | matakuliah | pengajar | hari | jam | status | catatan''' + '''\n'''
		message = "jadwal" + '''\n'''
		mycursor.execute("select * from jadwal_kuliah where konsentrasi='"+konsentrasi+"' or ks='"+konsentrasi+"'")
		results=mycursor.fetchall()

		for result in results: 
			message += "semester " + str(result[0]) + " " + str(result[2]) + " " + str(result[3]) + " " + str(result[4]) + " " + str(result[5]) + " " + str(result[7]) + " " + str(result[6]) + '''\n'''
			
		dispatcher.utter_message(text=message)

		return []


class ActionDaftarNilai(Action):

	def name(self) -> Text:
		return "action_daftar_nilai"

	def run(self, dispatcher: CollectingDispatcher,
	tracker: Tracker,
	domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		conn = pymysql.connect(host=os.environ.get('MYSQL_HOST'),user='root',database='chatbot_uii',port=3306,connect_timeout=5)
		mycursor = conn.cursor()

		try:
			nim = tracker.get_slot("NIM")
		except:
			nim = None

		try:	
			nama = tracker.get_slot("nama")
		except:
			nama = None 

		nama = nama.upper()

		message = "daftar nilai" + '''\n'''

		if nim is not None:
			mycursor.execute("select mata_kuliah, SKS, nilai from nilai_mahasiswa where NIM='"+nim+"'")
		else:
			mycursor.execute("select mata_kuliah, SKS, nilai from nilai_mahasiswa where nama='"+nama+"'")

		results=mycursor.fetchall()

		for result in results: 
			message += "mata kuliah " + str(result[0]) + " " + str(result[1]) + " " + str(result[2]) + '''\n'''
			
		dispatcher.utter_message(text=message)

		return []


class ActionJadwalSholat(Action):

	def name(self) -> Text:
		return "action_jadwal_sholat"

	def run(self, dispatcher: CollectingDispatcher,
	tracker: Tracker,
	domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		conn = pymysql.connect(host=os.environ.get('MYSQL_HOST'),user='root',database='chatbot_uii',port=3306,connect_timeout=5)
		mycursor = conn.cursor()

		kawasan = tracker.get_slot("kota")

		kawasan = kawasan.lower()

		mycursor.execute("select id from js_kota where nama_kota like '%"+kawasan+"%'")
		
		results=mycursor.fetchall()

		results_id = results[0][0]

		url = 'https://api.banghasan.com/sholat/format/json/jadwal/kota/{kota_id}/tanggal/{date_now}'.format(kota_id=results_id,date_now=datetime.strftime(datetime.now(),"%Y-%m-%d"))

		header = {'Content-Type': 'application/json'}

		response = requests.get(url, headers=header)

		results = response.json()

		msg_id = str(results['jadwal']['data']).replace("{","").replace("}","").replace(', ','\n').replace("'","")

		dispatcher.utter_message(text=msg_id)

		return []


class ActionPredCuaca(Action):

	def name(self) -> Text:
		return "action_pred_cuaca"

	def run(self, dispatcher: CollectingDispatcher,
	tracker: Tracker,
	domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		conn = pymysql.connect(host=os.environ.get('MYSQL_HOST'),user='root',database='chatbot_uii',port=3306,connect_timeout=5)
		mycursor = conn.cursor()

		kawasan = tracker.get_slot("kota")

		kawasan = kawasan.lower()

		mycursor.execute("select nama_kota from kota_indo where nama_kota like '%"+kawasan+"%'")
		
		results=mycursor.fetchall()

		results_kawasan = results[0][0]

		if len(results_kawasan.split()) > 1:
			kawasan_req = "%20".join(results_kawasan.split())
		else:
			kawasan_req = results_kawasan

		url = 'http://api.openweathermap.org/data/2.5/weather?q={kawasan},id&APPID={app_id}&units=metric'.format(kawasan=kawasan_req,app_id='9926258e5fbe65eb74b1eb220416b8d2')

		header = {'Content-Type': 'application/json'}

		response = requests.get(url, headers=header)

		results = response.json()

		msg_en = results['weather'][0]['description']

		global translator

		msg_id = translator.translate(msg_en, src='en', dest='id').text

		dispatcher.utter_message(text=msg_id)

		return []
