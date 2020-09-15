# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pymysql


class ActionDaftarJadwal(Action):

	def name(self) -> Text:
		return "action_daftar_jadwal"

	def run(self, dispatcher: CollectingDispatcher,
	tracker: Tracker,
	domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		conn = pymysql.connect(host='127.0.0.1',user='root',database='chatbot_uii',port=3306,connect_timeout=5)
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
