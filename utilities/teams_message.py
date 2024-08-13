import pymsteams


class TeamsMessage:

    def __init__(self, webhook: str, host: str, msg: list, icon: str = None):
        self.webhook: str = webhook
        self.host: str = host
        self.msg: list = msg

    def send_message(self):

        myTeamsMessage = pymsteams.connectorcard(self.webhook)

        myMessageSection = pymsteams.cardsection()

        myMessageSection.title(f"Logs from HOST: {self.host}")

        if self.icon:
            myMessageSection.activityImage(self.icon)

        myMessageSection.addFact("", "Process with errors:")
        try:
            for msg in self.msg:
                if msg:
                    myMessageSection.addFact("", msg.pop())
        except Exception as e:
            myMessageSection.addFact("", e)
        finally:
            myMessageSection.addFact("", "---------")

        myTeamsMessage.addSection(myMessageSection)
        myTeamsMessage.summary("---------")  # this step is required

        # Send message
        return myTeamsMessage.send()
