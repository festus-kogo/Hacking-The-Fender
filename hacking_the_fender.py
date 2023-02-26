# 1
import csv
import json
# 2
compromised_users = []

# 3
with open("passwords.csv", "r") as password_file:
  password_csv = csv.DictReader(password_file)
  # print(password_csv)
  # <csv.DictReader object at 0x7fb11663ce10>
  for password_row in password_csv:
    # print(password_row["Username"])
    # 7
    compromised_users.append(password_row["Username"])

# print(compromised_users)
# ['jean49', 'haydenashley', 'michaelastephens', 'denisephillips', 'andrew24', 'kaylaabbott', 'tmartinez', 'mholden', 'randygilbert', 'watsonlouis', 'mdavis', 'patrickprice', 'kgriffith', 'hannasarah', 'xaviermartin', 'hrodriguez', 'erodriguez', 'danielleclark', 'timothy26', 'elizabeth19']

# 8
with open("compromised_users.txt", "w") as compromised_user_file:
  for  compromised_user in compromised_users:
    # print(compromised_user)
    compromised_user_file.write(compromised_user)

with open("boss_message.json", "w") as boss_message:
  boss_message_dict = {
    "recipient": "The Boss",
    "message": "Mission Success"
  }
  json.dump(boss_message_dict, boss_message)

# 17
with open("new_passwords.csv", "w") as new_passwords_obj:
  slash_null_sig = """
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""
# print(slash_null_sig)

# 18
  writer = csv.writer(new_passwords_obj)

  # Write the data
  writer.writerow(slash_null_sig)