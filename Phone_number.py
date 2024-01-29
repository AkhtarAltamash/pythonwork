# import phonenumbers
# from phonenumbers import timezone,geocoder,carrier

# number=input("Enter Your Number. with +__: ")
# phone=phonenumbers.parse(number)
# time=timezone.time_zones_for_number(phone)
# carr=carrier.name_for_number(phone,"en")
# reg=geocoder.description_for_number(phone,"en")
# print(phone)
# print(time)
# print(carr)
# print(reg)


# ___________________________________

# import phonenumbers
# from phonenumbers import timezone,geocoder,carrier


# def get_valid_phone_number():
#     while True:
#         number = input("Enter Your Number (with +__): ")
#         try:
#             phone = phonenumbers.parse(number)
#             return phone
#         except phonenumbers.NumberParseException:
#             print("Invalid phone number. Please enter a valid number.")

# def get_timezone(phone):
#     try:
#         return timezone.time_zones_for_number(phone)
#     except phonenumbers.NumberFormatException:
#         return "Timezone information not available."

# def get_carrier(phone):
#     try:
#         return carrier.name_for_number(phone, "en")
#     except phonenumbers.NumberFormatException:
#         return "Carrier information not available."

# def get_region(phone):
#     try:
#         return geocoder.description_for_number(phone, "en")
#     except phonenumbers.NumberFormatException:
#         return "Region information not available."

# def print_formatted_output(phone, time, carr, reg):
#     print("Phone number:", phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL))
#     print("Timezone:", time)
#     print("Carrier:", carr)
#     print("Region:", reg)

# if __name__ == "__main__":
#     phone = get_valid_phone_number()
#     time = get_timezone(phone)
#     carr = get_carrier(phone)
#     reg = get_region(phone)

#     print_formatted_output(phone, time, carr, reg)
