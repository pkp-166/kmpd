import pyjokes
import pywhatkit
import wikipedia
import datetime
import openai

openai.api_key='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'

if __name__ == "__main__":
    print("Hello, Assistant here")
    while True:
            messages = []
            system_msg = 'sharp and formal'
            messages.append({"role": "system", "content": system_msg})
            print("Assistant is ready!.. press \'quit()\' to stop chatting.. ")
            command = input()
            messages.append({"role": "user", "content": command})
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages)
            reply = response["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": reply})
            if("I'm sorry" not in reply):
                print("\n" + reply + "\n")
            else:
                continue
            command=command.lower()
            if 'play' in command:
                song = command.replace('play','')
                pywhatkit.playonyt(song)
            elif (('search' or 'wiki' or 'wikipedia') in command):
                print(pywhatkit.info(command,lines=15))
                command2=input("\nDo you want to see the search results in google? ")
                if command2.lower()=='yes':
                    print(pywhatkit.search(command),"\n")
                else:
                    break
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                print('Current time is ' + time)
            elif 'who the heck is' in command:
                person = command.replace('who the heck is', '')
                info = wikipedia.summary(person, 1)
                print(info)
            elif (('joke' or 'jokes') in command):
                while(command!="no"):
                    print(pyjokes.get_joke())
                    command=input("Another one? ")
                    command=command.lower()

