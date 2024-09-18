import requests
import json

openai_key = ""

class AI:
    def __init__(self, key, system_prompt, model="gpt-4o-mini"):
        self.api_key = key
        self.system_prompt = system_prompt
        self.model = model

    def respond(self, user_prompt):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        body = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": self.system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        }
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, data=json.dumps(body))
        data = response.json()
        print(data['choices'][0]['message']['content'])
        return data['choices'][0]['message']['content']

ai = AI(openai_key, "Du er en robot som tar i mot et innlegg på engelsk. Du skal oversette innlegget til norsk. Ikke noe snikksnakk")

ai.respond("Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token.")

ai.respond("How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. Keep n as 1 to minimize costs.")

ai.respond("For all their extended drones, Sunn O))) have been about change. Soon after recording the heralded Grimm Robe Demos a decade ago, amp-and-volume addicts Stephen O'Malley and Greg Anderson had the good sense to realize that slow, distended riffs-- no matter how quaking, visceral, and charged-- could quickly wear down a band. To that end, Sunn O))) have collaborated with dozens of avant-garde and metal heavyweights over six full-lengths and a bevy of EPs, live takes, and joint releases. From noise paragon Merzbow and ex-Melvins/Earth grinder Joe Preston to contemporary allies Boris and Xasthur necro Malefic, an impressive horde have left their mark on Sunn O)))'s colossal doom.")

ai.respond("Dømkirke-- a vinyl-only, 2xLP set recorded in March 2007 in a 12th century Norwegian cathedral-- showcases Sunn O)))'s malleability and versatility. Here, Anderson and O'Malley are assisted by four auxiliary members: Attila Csihar, the enigmatic vocalist of black metal band Mayhem; Steve Moore, the Southern Lord horns-and-keyboards specialist who now plays in Earth full time; longtime Sunn O))) collaborator Tos Nieuwenhuizen; and Lasse Marhaug, an Oslo electronicist whose work as Jazkamer spun glorious noise from metal threads on 2006's Metal Music Machine. The Borealis Festival-- an artistically adventurous affair spread throughout venues in Bergen, Norway's second city-- commissioned the piece to mirror the gothic Gregorian hymns of the Late Middle Ages... [which] reflected the despair, the terrors and darkness of the world. Oh, the irony and possibilities...")