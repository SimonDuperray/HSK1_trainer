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
               to_return = "Vous avez eu bon 25 fois ?? ce mot ! Il est consid??r?? comme acquis ! Bravo !"
               break
   return to_return

caratteres = [
   {
      'fr': 'un',
      'ch': 'y??',
      'py': '???'
   },
   {
      'fr': 'deux',
      'ch': '??r',
      'py': '???'
   },
   {
      'fr': 'trois',
      'ch': 's??n',
      'py': '???'
   },
   {
      'fr': 'quatre',
      'ch': 's??',
      'py': '???'
   },
   {
      'fr': 'cinq',
      'ch': 'w??',
      'py': '???'
   },
   {
      'fr': 'six',
      'ch': 'li??',
      'py': '???'
   },
   {
      'fr': 'sept',
      'ch': 'q??',
      'py': '???'
   },
   {
      'fr': 'huit',
      'ch': 'b??',
      'py': '???'
   },
   {
      'fr': 'neuf',
      'ch': 'ji??',
      'py': '???'
   },
   {
      'fr': 'dix',
      'ch': 'sh??',
      'py': '???'
   },
   {
      'fr': 'aimer; affectionner; ??tre friand de; amour',
      'ch': '??i',
      'py': '???'
   },
   {
      'fr': 'manger; avoir son repas',
      'ch': 'ch??',
      'py': '???'
   },
   {
      'fr': 't??l??phoner',
      'ch': 'd?? di??n hu??',
      'py': '?????????'
   },
   {
      'fr': 'boire; crier (un ordre)',
      'ch': 'h??',
      'py': '???'
   },
   {
      'fr': 'revenir; faire demi-tour; r??pondre; revenir; tourner; Groupe ethnique Hui; temps; classificateur des actes d\'une pi??ce; section ou chapitre (d\'un livre classique)',
      'ch': 'hu??',
      'py': '???'
   },
   {
      'fr': '(s\') appeler; crier; ordonner; demander; appeler; par',
      'ch': 'ji??o',
      'py': '???'
   },
   {
      'fr': 'ouvrir; commencer; allumer; conduire (un v??hicule)',
      'ch': 'k??i',
      'py': '???'
   },
   {
      'fr': 'regarder',
      'ch': 'k??n',
      'py': '???'
   },
   {
      'fr': 'voir; apercevoir',
      'ch': 'k??n ji??n',
      'py': '??????'
   },
   {
      'fr': 'venir; arriver; se rallier; depuis; suivant',
      'ch': 'l??i',
      'py': '???'
   },
   {
      'fr': 'p??re',
      'ch': 'b?? ba',
      'py': '??????'
   },
   {
      'fr': 'tasse; verre;',
      'ch': 'b??i zi',
      'py': '??????'
   },
   {
      'fr': 'Beijing; P??kin',
      'ch': 'b??i j??ng',
      'py': '??????'
   },
   {
      'fr': 'origine; source; racine; tiges des plantes; fondation; base; classificateur pour les livres, les p??riodiques, les fichiers, etc; initialement',
      'ch': 'b??n',
      'py': '???'
   },
   {
      'fr': 'ne pas (pr??fixe n??gatif); pas; aucun',
      'ch': 'b??',
      'py': '???'
   },
   {
      'fr': 'Je vous en prie; de rien',
      'ch': 'b?? k?? qi',
      'py': '?????????'
   },
   {
      'fr': 'plat (aliments); l??gumes; cuisine',
      'ch': 'c??i',
      'py': '???'
   },
   {
      'fr': 'th??; feuille de th??',
      'ch': 'ch??',
      'py': '???'
   },
   {
      'fr': 'taxi',
      'ch': 'ch?? z?? ch??',
      'py': '?????????'
   },
   {
      'fr': 'grand; important; large; le plus ancien; a??n??',
      'ch': 'd??',
      'py': '???'
   },
   {
      'fr': 'de (particule de possession ou de description)',
      'ch': 'de',
      'py': '???'
   },
   {
      'fr': 'un peu; certain; goutte (de liquide); tache; rep??rer; grain; noter; virgule (en caract??res chinois); point d??cimal; marque (de degr?? ou niveau); une place (avec certaines caract??ristiques); heures; aborder bri??vement; pr??ciser; la lumi??re; allumer; p??riode de temps pendant la nuit (24 minutes) (ancien); un goutte ?? goutte; plantoir; classificateur des petites quantit??s ind??termin??es',
      'ch': 'di??n',
      'py': '???'
   },
   {
      'fr': 'ordinateur',
      'ch': 'di??n n??o',
      'py': '??????'
   },
   {
      'fr': 't??l??vision',
      'ch': 'di??n sh??',
      'py': '??????'
   },
   {
      'fr': 'film',
      'ch': 'di??n y??ng',
      'py': '??????'
   },
   {
      'fr': 'chose; des trucs; personne (p??joratif)',
      'ch': 'd??ng xi',
      'py': '??????'
   },
   {
      'fr': 'tous; tout; enti??rement (?? cause de) chacune; m??me; d??j??',
      'ch': 'd??u',
      'py': '???'
   },
   # {
   #    'fr': 'lire; ??tudier; lecture de mot (par exemple la prononciation), similaire ?? ??????[pin1 yin1]',
   #    'ch': 'd??',
   #    'py': '???'
   # },
   # {
   #    'fr': 'Je suis d??sol??; Excusez-moi; s\'il vous pla??t; d??sol??? (s\'il vous pla??t r??p??ter); indigne; laisser tomber;',
   #    'ch': 'du?? bu q??',
   #    'py': '?????????'
   # },
   {
      'fr': 'beaucoup; nombreux; multi-',
      'ch': 'du??',
      'py': '???'
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
      print(colored(f">>> Fin de la s??rie !\n>>> R??sultats: {final_percent}% de bonnes r??ponses ({correct} correctes/{not_correct} incorrectes)", "green"))
      if final_percent>max(get_best_score()):
         print(">>> Nouveau meilleure score ! Bravo !")
      elif final_percent>=max(get_best_score()):
         print(f">>> Tu viens d'??galiser ton meilleur score actuel pour la {get_occ_best_score(final_percent)}eme fois !")
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