import requests
import json

# Base URL of the Flask API
BASE_URL = 'http://127.0.0.1:5000/api/users/'

# Function to send a request and log the result
def send_request(method, endpoint, data=None):
    url = BASE_URL + endpoint
    headers = {'Content-Type': 'application/json'}
    response = requests.request(method, url, json=data, headers=headers)
    result = response.json() if response.text else {}
    log_result({'method': method, 'endpoint': endpoint, 'response': result})
    return result

# Helper function to log results to results.txt in JSON format
def log_result(data):
    with open('results.txt', 'a') as f:
        f.write(json.dumps(data) + "\n")

if __name__ == '__main__':
    # Retrieve all existing students (GET)
    all_students_before = send_request('GET', '')

    # Create three students (POST)
    student1 = {'user_name': 'Alice', 'user_lastname': 'Smith', 'user_age': '25'}
    student2 = {'user_name': 'Bob', 'user_lastname': 'Johnson', 'user_age': '28'}
    student3 = {'user_name': 'Charlie', 'user_lastname': 'Brown', 'user_age': '30'}

    created_student1 = send_request('POST', '', data=student1)
    created_student2 = send_request('POST', '', data=student2)
    created_student3 = send_request('POST', '', data=student3)

    # Retrieve information about all existing students (GET)
    all_students_after_creation = send_request('GET', '')

    # Update the age of the second student (PATCH)
    updated_age_student2 = {'user_age': '29'}
    updated_student2 = send_request('PATCH', f'{created_student2["id"]}', data=updated_age_student2)

    # Retrieve information about the second student (GET)
    student2_info = send_request('GET', f'{created_student2["id"]}')

    # Update the first name, last name, and age of the third student (PUT)
    updated_info_student3 = {'user_name': 'Charlie Updated', 'user_lastname': 'Brown Updated', 'user_age': '31'}
    updated_student3 = send_request('PUT', f'{created_student3["id"]}', data=updated_info_student3)

    # Retrieve information about the third student (GET)
    student3_info = send_request('GET', f'{created_student3["id"]}')

    # Retrieve all existing students (GET)
    all_students_after_updates = send_request('GET', '')

    # Delete the first user (DELETE)
    delete_result = send_request('DELETE', f'{created_student1["id"]}')

    # Retrieve all existing students after deletion (GET)
    all_students_after_deletion = send_request('GET', '')

    # Display execution results in the console and write them to results.txt
    print("All Students Before Creation:", all_students_before)
    print("Created Student 1:", created_student1)
    print("Created Student 2:", created_student2)
    print("Created Student 3:", created_student3)
    print("All Students After Creation:", all_students_after_creation)
    print("Updated Student 2:", updated_student2)
    print("Info of Student 2:", student2_info)
    print("Updated Student 3:", updated_student3)
    print("Info of Student 3:", student3_info)
    print("All Students After Updates:", all_students_after_updates)
    print("Delete Result:", delete_result)
    print("All Students After Deletion:", all_students_after_deletion)

    # Log results to results.txt
    log_result({"message": "All Students Before Creation", "data": all_students_before})
    log_result({"message": "Created Student 1", "data": created_student1})
    log_result({"message": "Created Student 2", "data": created_student2})
    log_result({"message": "Created Student 3", "data": created_student3})
    log_result({"message": "All Students After Creation", "data": all_students_after_creation})
    log_result({"message": "Updated Student 2", "data": updated_student2})
    log_result({"message": "Info of Student 2", "data": student2_info})
    log_result({"message": "Updated Student 3", "data": updated_student3})
    log_result({"message": "Info of Student 3", "data": student3_info})
    log_result({"message": "All Students After Updates", "data": all_students_after_updates})
    log_result({"message": "Delete Result", "data": delete_result})
    log_result({"message": "All Students After Deletion", "data": all_students_after_deletion})
