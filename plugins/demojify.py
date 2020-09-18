import pinhook.plugin as p
import emoji

@p.listener('demojify')
def demojify(msg):
    demojized_text = emoji.demojize(msg.text)
    if demojized_text != msg.text and msg.nick != 'pinhook':
        return p.message('<{}> {}'.format(msg.nick, demojized_text))
