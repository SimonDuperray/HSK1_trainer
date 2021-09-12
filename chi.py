from random import randint
import json, time

def gen_equals(nb_of_eq):
   to_return = ""
   for i in range(0, nb_of_eq+19):
      to_return += "="
   return to_return

def percent_correct(len_init, correct):
   return int(100*correct/len_init)

def create_timestamp(second_since_epoch, time_object):
   return '%d-%d-%d//%d:%d:%d' % (timeObj.tm_mday, timeObj.tm_mon, timeObj.tm_year, timeObj.tm_hour, timeObj.tm_min, timeObj.tm_sec)

def save_results(new_data, filename='results.json'):
   with open(filename, 'r+') as file:
      # serie
      existing_data = json.load(file)
      existing_data["series"].append(new_data)
      file.seek(0)
      # score
      buffer = None
      current_stocked_scores = existing_data["scores"]
      for k in range(len(current_stocked_scores)):     
         if current_stocked_scores[k]['score']==data['percent']:
            buffer = current_stocked_scores[k]
            break

      if buffer is not None:
         buffer['occ']+=1
      else:
         current_stocked_scores.append(
            {
               "score": data['percent'],
               "occ": 1
            }
         )
      json.dump(existing_data, file, indent=3)

def get_best_score(filename="results.json"):
   with open(filename, 'r') as file:
      data = json.load(file)["series"]
      percent_list = []
      for i in range(len(data)):
         percent_list.append(data[i]['percent'])
   return percent_list

def get_occ_best_score(current_score, filename='results.json'):
   to_return = 0
   with open(filename, "r") as file:
      data = json.load(file)['scores']
      for k in range(len(data)):
         if current_score == int(data[k]['score']):
            to_return = data[k]['occ']+1
   return to_return

caratteres = [
   {
      'fr': 'un',
      'ch': 'yī',
      'py': '一'
   },
   {
      'fr': 'deux',
      'ch': 'èr',
      'py': '二'
   },
   {
      'fr': 'trois',
      'ch': 'sān',
      'py': '三'
   },
   {
      'fr': 'quatre',
      'ch': 'sì',
      'py': '四'
   },
   {
      'fr': 'cinq',
      'ch': 'wǔ',
      'py': '五'
   },
   {
      'fr': 'six',
      'ch': 'liù',
      'py': '六'
   },
   {
      'fr': 'sept',
      'ch': 'qī',
      'py': '七'
   },
   {
      'fr': 'huit',
      'ch': 'bā',
      'py': '八'
   },
   {
      'fr': 'neuf',
      'ch': 'jiǔ',
      'py': '九'
   },
   {
      'fr': 'dix',
      'ch': 'shí',
      'py': '十'
   },
   {
      'fr': 'aimer; affectionner; être friand de; amour',
      'ch': 'ài',
      'py': '爱'
   },
   {
      'fr': 'manger; avoir son repas',
      'ch': 'chī',
      'py': '吃'
   },
   {
      'fr': 'téléphoner',
      'ch': 'dǎ diàn huà',
      'py': '打电话'
   },
   {
      'fr': 'boire; crier (un ordre)',
      'ch': 'hē',
      'py': '喝'
   },
   {
      'fr': 'revenir; faire demi-tour; répondre; revenir; tourner; Groupe ethnique Hui; temps; classificateur des actes d\'une pièce; section ou chapitre (d\'un livre classique)',
      'ch': 'huí',
      'py': '回'
   },
   {
      'fr': '(s\') appeler; crier; ordonner; demander; appeler; par (indique l\'agent dans la mode passive)',
      'ch': 'jiào',
      'py': '叫'
   },
   {
      'fr': 'ouvrir; commencer; allumer; conduire (un véhicule)',
      'ch': 'kāi',
      'py': '开'
   },
   {
      'fr': 'regarder',
      'ch': 'kàn',
      'py': '看'
   },
   {
      'fr': 'voir; apercevoir',
      'ch': 'kàn jiàn',
      'py': '看见'
   },
   {
      'fr': 'venir; arriver; se rallier; depuis; suivant',
      'ch': 'lái',
      'py': '来'
   },
]
lngs = ['fr', 'ch', 'py']
init_len = len(caratteres)
correct, not_correct = 0, 0
secondsSinceEpoch = time.time()
timeObj = time.localtime(secondsSinceEpoch)

for i in range(0, init_len):
   idx = randint(0, init_len-1-i)
   lng = lngs[randint(0, 2)]
   rdm = caratteres[idx][lng]
   print(f"{gen_equals(len(rdm))}\n > [{i+1}-{init_len}] -> {lng}: {rdm}\n{gen_equals(len(rdm))}")
   del caratteres[idx]
   is_correct = input("correct [*] / incorrect [n] ? ")
   if is_correct=="n":
      not_correct+=1
   else:
      correct += 1
   if i+1 == init_len:
      final_percent = percent_correct(init_len, correct)
      print(f">>> Fin de la série !\n>>> Résultats: {final_percent}% de bonnes réponses ({correct} correctes/{not_correct} incorrectes)")
      if final_percent>max(get_best_score()):
         print(">>> Nouveau meilleure score ! Bravo !")
      elif final_percent>=max(get_best_score()):
         print(f">>> Tu viens d'égaliser ton meilleur score actuel pour la {get_occ_best_score(final_percent)}eme fois !")
   else:
      pass

data = {
   'id': create_timestamp(secondsSinceEpoch, timeObj),
   'correct': correct,
   'incorrect': not_correct,
   'len': init_len,
   'percent': percent_correct(init_len, correct)
}

save_results(data)