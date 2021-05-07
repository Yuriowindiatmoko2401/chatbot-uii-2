from rasa.core.channels.socketio import SocketIOInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa.utils.endpoints import EndpointConfig
# from MyIo import RestInput


action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")

# load your trained agent
nlu_interpreter = RasaNLUInterpreter('/home/yurio/kuliah/thesis_mania/mi-botway/chatbot-uii-2/models/20210502-232800/nlu')
agent = Agent.load('/home/yurio/kuliah/thesis_mania/mi-botway/chatbot-uii-2/models/20210502-232800/core', interpreter=nlu_interpreter, action_endpoint=action_endpoint)

input_channel = SocketIOInput(
            # event name for messages sent from the user
            user_message_evt="user_uttered",
            # event name for messages sent from the bot
            bot_message_evt="bot_uttered",
            # socket.io namespace to use for the messages
            namespace=None
    )

# set serve_forever=False if you want to keep the server running
s = agent.handle_channels([input_channel], 5005)