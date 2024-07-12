
# REST API (homework 12)

# GET
- By their ID; if the provided ID is not found in the database, return an error.
![Alt text](/assets/user_not_found.png)
- By their last name; if there are multiple students with the same last name, display all of them; if the provided last name is not found in the database, return an error.
![Alt text](/assets/get_lastname.png)
![Alt text](/assets/get_lastname_few_same_users.png)
![Alt text](/assets/get_user_not_found.png)
- Retrieve a list of all students (display all available information).
![Alt text](/assets/get_all_users.png)
# POST
- The ID field should be automatically generated with an increment of +1.
![Alt text](/assets/auto_increment.png)
- The POST request body should include first name, last name, and age.
![Alt text](/assets/post_lack_fields_error.png)
- If a non-existing field is passed in the POST body or if no fields are passed at all, return an error.
![Alt text](/assets/post_not_alowed_field.png)
![Alt text](/assets/post_all_missed.png)
- If any of the fields are missing in the POST body, return an error without writing to the CSV file.
![Alt text](/assets/post_missed_field.png)
- Upon successful request, return information about the added student.
![Alt text](/assets/post_success_created.png)
# PUT
- It should be possible to update the fields first name, last name, and age.
![Alt text](/assets/before_put.png)
![Alt text](/assets/after_put.png)
- If the provided ID is not found in the database, return an error.
![Alt text](/assets/put_not_found.png)
- The PUT request body should include first name, last name, and age accordingly.
![Alt text](/assets/put_required_all_fields.png)
- If a non-existing field is passed in the PUT body or if no fields are passed at all, return an error.
![Alt text](/assets/put_not_alowed_field.png)
![Alt text](/assets/put_no_fields.png)
- Upon successful request, return the updated information about the student.
![Alt text](/assets/after_put.png)
# PATCH
- It should be possible to update the age field.
![Alt text](/assets/before_patch.png)
![Alt text](/assets/after_patch.png)
- If the provided ID is not found in the database, return an error.
![Alt text](/assets/patch_not_found.png)
- The PATCH request body should include the age.
![Alt text](/assets/patch_not_alowed_field.png)
- If a non-existing field is passed in the PATCH body or if no fields are passed at all, return an error.
![Alt text](/assets/patch_not_alowed_field.png)
![Alt text](/assets/patch_empty_request.png)
- Upon successful request, return the updated information about the student.
![Alt text](/assets/before_patch.png)
![Alt text](/assets/after_patch.png)
# DELETE
- If the provided ID is not found in the CSV file, return an error.
![Alt text](/assets/del_not_found.png)
- Upon successful request, return a message confirming the successful deletion of the student.
![Alt text](/assets/del_success.png)