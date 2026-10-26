

def login(user_data):
    print(f"{user_data ['name']} loged in ")
   
def viwe(user_data):
    print(f"{user_data['name']} is viweing the task")
    
def submit_task(user_data):
    if user_data['roll']== "team_member":
        print(f"{user_data['name']} has submitted task");
    else:
        print("manager no need to submitt")

    
def assign_task(user_data):
    if user_data['roll']== "manager":
        print(f"{user_data['name']} has assgin task");
    else:
        print("team member the task need to submitt")

    




user_data={"name":"sam","roll":"manager"}

login(user_data)
viwe(user_data)
submit_task(user_data)
assign_task(user_data)

