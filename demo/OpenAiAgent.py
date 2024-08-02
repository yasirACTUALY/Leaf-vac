from openai import OpenAI


  
client = OpenAI(api_key='')
# client = OpenAI()

while True:
    # take in user input
    user_input = input("User: ")
    if(user_input == "quit") or (user_input == "q"):
        break

    cameraOutput = input("Camera: ")
    print("Human command: " + user_input + "   Camera:  " + cameraOutput)
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are piloting a robot wth a camera. return [] with the direction of movement/turning to move it."},
        {"role": "user", "content": "Human command: " + user_input + "   Camera:  " + cameraOutput}
    ]
    )

    print(completion.choices[0].message)

