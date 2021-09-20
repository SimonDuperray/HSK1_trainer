from random import randint
from termcolor import colored
import json, time, random

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

def get_evolution(word, filename='results.json'):
   with open(filename, 'r') as file:
      existing_data = json.load(file)
      buffer = None
      current_stocked_evolutions = existing_data['evolution']
      for k in range(len(current_stocked_evolutions)):
         if current_stocked_evolutions[k]['word']==word:
            buffer = current_stocked_evolutions[k]
            break
      if buffer is not None:
         buffer['nb_correct']+=1
      else:
         current_stocked_evolutions.append(
            {
               "word": word,
               "nb_correct": 0
            }
         )
      return existing_data

def replace_data_in_file(data, filename='results.json'):
   with open(filename, 'w') as file:
      json.dump(data, file, indent=3)
      
def check_if_learned(word, filename='results.json'):
   to_return = None
   with open(filename, "r") as file:
      data = json.load(file)['evolution']
      for i in range(len(data)):
         if data[i]['word']==word:
            if data[i]['nb_correct']==25:
               # 17
               to_return = "Vous avez eu bon 25 fois à ce mot ! Il est considéré comme acquis ! Bravo !"
               break
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
      'fr': '(s\') appeler; crier; ordonner; demander; appeler; par',
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
   {
      'fr': 'père',
      'ch': 'bà ba',
      'py': '爸爸'
   },
   {
      'fr': 'tasse; verre;',
      'ch': 'bēi zi',
      'py': '杯子'
   },
   {
      'fr': 'Beijing; Pékin',
      'ch': 'běi jīng',
      'py': '北京'
   },
   {
      'fr': 'origine; source; racine; tiges des plantes; fondation; base; classificateur pour les livres, les périodiques, les fichiers, etc; initialement',
      'ch': 'běn',
      'py': '本'
   },
   {
      'fr': 'ne pas (préfixe négatif); pas; aucun',
      'ch': 'bù',
      'py': '不'
   },
   {
      'fr': 'Je vous en prie; de rien',
      'ch': 'bú kè qi',
      'py': '不客气'
   },
   {
      'fr': 'plat (aliments); légumes; cuisine',
      'ch': 'cài',
      'py': '菜'
   },
   {
      'fr': 'thé; feuille de thé',
      'ch': 'chá',
      'py': '茶'
   },
   {
      'fr': 'taxi',
      'ch': 'chū zū chē',
      'py': '出租车'
   },
   {
      'fr': 'grand; important; large; le plus ancien; aîné',
      'ch': 'dà',
      'py': '大'
   },
   {
      'fr': 'de (particule de possession ou de description)',
      'ch': 'de',
      'py': '的'
   },
   {
      'fr': 'un peu; certain; goutte (de liquide); tache; repérer; grain; noter; virgule (en caractères chinois); point décimal; marque (de degré ou niveau); une place (avec certaines caractéristiques); heures; aborder brièvement; préciser; la lumière; allumer; période de temps pendant la nuit (24 minutes) (ancien); un goutte à goutte; plantoir; classificateur des petites quantités indéterminées',
      'ch': 'diǎn',
      'py': '点'
   },
   {
      'fr': 'ordinateur',
      'ch': 'diàn nǎo',
      'py': '电脑'
   },
   {
      'fr': 'télévision',
      'ch': 'diàn shì',
      'py': '电视'
   },
   {
      'fr': 'film',
      'ch': 'diàn yǐng',
      'py': '电影'
   },
   {
      'fr': 'chose; des trucs; personne (péjoratif)',
      'ch': 'dōng xi',
      'py': '东西'
   },
   {
      'fr': 'tous; tout; entièrement (à cause de) chacune; même; déjà',
      'ch': 'dōu',
      'py': '都'
   },
   # {
   #    'fr': 'lire; étudier; lecture de mot (par exemple la prononciation), similaire à 拼音[pin1 yin1]',
   #    'ch': 'dú',
   #    'py': '读'
   # },
   # {
   #    'fr': 'Je suis désolé; Excusez-moi; s\'il vous plaît; désolé? (s\'il vous plaît répéter); indigne; laisser tomber;',
   #    'ch': 'duì bu qǐ',
   #    'py': '对不起'
   # },
   {
      'fr': 'beaucoup; nombreux; multi-',
      'ch': 'duō',
      'py': '多'
   }
]
lngs = ['fr', 'ch', 'py']
init_len = len(caratteres)
correct, not_correct = 0, 0
secondsSinceEpoch = time.time()
timeObj = time.localtime(secondsSinceEpoch)

for i in range(0, init_len):
   idx = randint(0, init_len-1-i)
   lng = lngs[randint(0, 2)]
   if lng=='fr':
      rdm = random.choice([cara.strip() for cara in caratteres[idx][lng].split(";")])
   else:
      rdm = caratteres[idx][lng]
   print(colored(f"{gen_equals(len(rdm))}\n > [{i+1}-{init_len}] -> {lng}: {rdm}\n{gen_equals(len(rdm))}", "blue"))
   print_correct = input("Enter to show correction !")
   if print_correct is not None:
      buffer = random.choice(caratteres[idx]['fr'].split(';'))
      print(colored(f">>> Correction: fr -> {caratteres[idx]['fr']}: ch -> {caratteres[idx]['ch']}: py -> {caratteres[idx]['py']}", "cyan"))
   del caratteres[idx]
   is_correct = input("correct [*] / incorrect [n] ? ")
   if is_correct=="n":
      not_correct+=1
   else:
      correct += 1
      replace_data_in_file(get_evolution(buffer))
      is_learned = check_if_learned(buffer)
      if is_learned is not None:
        print(colored((">>> "+is_learned), "yellow"))
   if i+1 == init_len:
      final_percent = percent_correct(init_len, correct)
      print(colored(f">>> Fin de la série !\n>>> Résultats: {final_percent}% de bonnes réponses ({correct} correctes/{not_correct} incorrectes)", "green"))
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