from en_alphabet_class import EngAlphabet 
from ua_alphabet_class import UaAlphabet
from prettytable import PrettyTable

eng_2 = EngAlphabet()
ua_2 = UaAlphabet()


test_table = PrettyTable()
test_table.field_names = ["func / classes", "EN_Alphabet_class", "UA_Alphabet_class"]
test_table.add_row(["print()", eng_2.print_letters(), ua_2.print_letters()])
test_table.add_row(["amouunt_of_letters()", eng_2.amouunt_of_letters(), ua_2.amouunt_of_letters()])
test_table.add_row(["is_en_letter('F')", eng_2.is_en_letter('F'), "-"])
test_table.add_row(["is_en_letter('Щ')", eng_2.is_en_letter('Щ'), "-"])
test_table.add_row(["is_ua_letter('F')", "-", ua_2.is_ua_letter('F')])
test_table.add_row(["is_ua_letter('Щ')", "-", ua_2.is_ua_letter('Щ')])
test_table.add_row(["random_letter()", eng_2.random_letter(), ua_2.random_letter()])
test_table.add_row(["is_in_alphabet('R')", eng_2.is_in_alphabet('R'), ua_2.is_in_alphabet('R')])
test_table.add_row(["is_in_alphabet('Ю')", eng_2.is_in_alphabet('Ю'), ua_2.is_in_alphabet('Ю')])
test_table.add_row(["example()", eng_2.example(), ua_2.example()])
print(test_table)
print(eng_2.example())












