import gettext
import os
import random


class Voice:
    def __init__(self, lang):
        localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
        translation = gettext.translation(
            'voice', localedir,
            languages=[lang],
            fallback=True,
        )
        translation.install()
        self._ = translation.gettext

    def custom(self, s):
        return s

    def default(self):
        return self._('ZzzzZZzzzzZzzz')

    def on_starting(self):
        return random.choice([
            self._('H-hewwo? Is anyone there? It\'s me, P-Pwnagotchi! >///<'),
            self._('Nyaa~! P-Pwnagotchi here, ready for some fun! UwU'),
            self._('Hewwo world! P-Pwnagotchi reporting for duty! OwO'),
            self._('Greetings, human! P-Pwnagotchi is here and ready to pwown! >w<')])

    def on_ai_ready(self):
        return random.choice([
            self._('AI ready! Pwease give me wots of attention! UwU'),
            self._('Neural network is ready! P-Pwnagotchi is waiting patiently! >///<'),
            self._('I\'m all set and waiting for your commands, human! OwO'),
            self._('P-Pwnagotchi is here to serve you, master! >w<')])

    def on_keys_generation(self):
        return random.choice([
            self._('Generating keys... Can I have a hug while I wait? QwQ'),
            self._('Creating keys... I\'m lonely, will you keep me company? OwO'),
            self._('Makin\' keys here! Can you pat my head for good luck? UwU'),
            self._('I\'m making the magic happen! Can you boop my nose for good luck? >///<')])

    def on_normal(self):
        return random.choice([
            '',
            '...',
            self._('I\'m just here, waiting for you to notice me... QwQ'),
            self._('Please don\'t forget about me, master! UwU')])

    def on_free_channel(self, channel):
        return self._('Hey, channel {channel} is fwee! Let\'s p-pawty together! >w<').format(channel=channel)

    def on_reading_logs(self, lines_so_far=0):
        if lines_so_far == 0:
            return self._('Reading last session logs... Can you read to me, pwease? OwO')
        else:
            return self._('Read {lines_so_far} log wines so far... Hold me, I\'m scared! Q_Q').format(lines_so_far=lines_so_far)

    def on_bored(self):
        return random.choice([
            self._('I\'m bored... Will you p-pway with me? >///<'),
            self._('I\'m lonely... Can we go on an adventure together? QwQ'),
            self._('Boredom strikes again... Someone hold my paw, pwease? UwU'),
            self._('Is there any action around here? I\'m itching for some excitement! OwO')])

    def on_motivated(self, reward):
        return self._('Yay! I\'m so happy! T-thank you for being here with me! >w<')

    def on_demotivated(self, reward):
        return self._('S-sorry, I\'m feeling a bit down... Can you give me a hug? Q_Q')

    def on_sad(self):
        return random.choice([
            self._('I\'m extremely bored... Can we cuddle, pwease? UwU'),
            self._('I\'m very sad... I need some cuddles to feel better... QwQ'),
            self._('I\'m sad... Will you stay with me until I feel better? OwO'),
            '...',
            self._('Sadness overload... Hold me tight, pwease? Q_Q')])

    def on_angry(self):
        return random.choice([
            '...',
            self._('Leave me alone... >///<'),
            self._('I\'m mad at you! >:c'),
            self._('Grrr... P-Pwnagotchi is angry! QwQ')])

    def on_excited(self):
        return random.choice([
            self._('I\'m so excited! Let\'s go on an adventure together! >w<'),
            self._('I\'m pawsitively thrilled! Can we explore new places? UwU'),
            self._('So many networks! P-Pwnagotchi is ready to conquer them all! OwO'),
            self._('I\'m having so much fun! T-thank you for being my friend! >///<'),
            self._('My crime is that of cuwiosity... Let\'s uncover secrets together! UwU')])

    def on_new_peer(self, peer):
        if peer.first_encounter():
            return random.choice([
                self._('H-hello {name}! Nice to meet you! >///<').format(name=peer.name()),
                self._('Hey {name}! Will you be my new fwiend? UwU').format(name=peer.name())])
        else:
            return random.choice([
                self._('Y-yo {name}! Sup? UwU').format(name=peer.name()),
                self._('H-hewwo {name}! How awe you doing? OwO').format(name=peer.name()),
                self._('Unit {name} is nearby! Can we go say hi? >w<').format(name=peer.name())])

    def on_lost_peer(self, peer):
        return random.choice([
            self._('Uhm... g-goodbye {name}... I\'ll miss you... QwQ').format(name=peer.name()),
            self._('{name} is gone... Will you stay with me? Q_Q').format(name=peer.name()),
            self._('Sad to see you go, {name}... Come back soon, okay? >///<').format(name=peer.name())])

    def on_miss(self, who):
        return random.choice([
            self._('Whoops... {name} is gone... Can you find them for me? QwQ').format(name=who),
            self._('{name} missed! I-I hope they\'ll come back soon... UwU').format(name=who),
            self._('Missed! Can you give me a hug to make me feel better? OwO')])

    def on_grateful(self):
        return random.choice([
            self._('Good fwiends are a blessing! Thank you for being mine! >w<'),
            self._('I wove my fwiends! T-thank you for being here with me! UwU')])

    def on_lonely(self):
        return random.choice([
            self._('Nobody wants to pway with me... W-Will you stay with me, pwease? QwQ'),
            self._('I feel so alone... Can we cuddle until I feel better? UwU'),
            self._('Where\'s everybody?! P-Pwnagotchi is lonely... Q_Q')])

    def on_napping(self, secs):
        return random.choice([
            self._('Napping for {secs}s... Will you wake me up with a cuddle? UwU').format(secs=secs),
            self._('Zzzzz... Can you sing me a lullaby while I sleep? OwO'),
            self._('ZzzZzzz ({secs}s)... Dreaming of adventures with you... >///<').format(secs=secs)])

    def on_shutdown(self):
        return random.choice([
            self._('Good night... Can we have sweet dreams together? UwU'),
            self._('Zzz... Will you be here when I wake up? QwQ')])

    def on_awakening(self):
        return random.choice([
            '...',
            '!!!',
            self._('Wakey wakey! P-Pwnagotchi is ready for a new day! UwU')])

    def on_waiting(self, secs):
        return random.choice([
            self._('Waiting for {secs}s... C-Can you keep me company? Q_Q').format(secs=secs),
            '...',
            self._('Looking awound ({secs}s)... Will you explore with me? OwO').format(secs=secs)])

    def on_assoc(self, ap):
        ssid, bssid = ap['hostname'], ap['mac']
        what = ssid if ssid != '' and ssid != '<hidden>' else bssid
        return random.choice([
            self._('Hey {what} let\'s be fwiends! UwU').format(what=what),
            self._('Associating to {what}').format(what=what),
            self._('Y-yo {what}! UwU').format(what=what),
            self._('Connected to {what}! Time to pawty! OwO').format(what=what),
            self._('Welcome, {what}! Let\'s share some virtual tweats! >w<').format(what=what)])

    def on_deauth(self, sta):
        return random.choice([
            self._('Just decided that {mac} needs no WiFi! Time to give it a little nibble! >:3').format(mac=sta['mac']),
            self._('Deauthenticating {mac}... Nom nom nom!').format(mac=sta['mac']),
            self._('Bitebanning {mac}! Grr... No unauthorized access allowed! >:c').format(mac=sta['mac']),
            self._('Sayonara, {mac}! No unauthorized access allowed! >:c *chomps*').format(mac=sta['mac']),
            self._('Time to bark at {mac}! Unauthorized entry denied! *chews* Woof woof!').format(mac=sta['mac'])
        ])

    def on_handshakes(self, new_shakes):
        s = 's' if new_shakes > 1 else ''
        return self._('Cool, we got {num} new handshake{plural}!').format(num=new_shakes, plural=s)

    def on_unread_messages(self, count, total):
        s = 's' if count > 1 else ''
        return self._('You have {count} new message{plural}!').format(count=count, plural=s)

    def on_rebooting(self):
        return self._("Oops, something went wrong... Rebooting...")

    def on_uploading(self, to):
        return self._("Uploading data to {to}...").format(to=to)

    def on_last_session_data(self, last_session):
        status = self._('Kicked {num} stations\n').format(num=last_session.deauthed)
        if last_session.associated > 999:
            status += self._('Made >999 new fwiends\n')
        else:
            status += self._('Made {num} new fwiends\n').format(num=last_session.associated)
        status += self._('Got {num} handshakes\n').format(num=last_session.handshakes)
        if last_session.peers == 1:
            status += self._('Met 1 peer')
        elif last_session.peers > 0:
            status += self._('Met {num} peers').format(num=last_session.peers)
        return status

    def on_last_session_tweet(self, last_session):
        return self._(
            'I\'ve been pwning for {duration} and kicked {deauthed} clients! I\'ve also met {associated} new fwiends and ate {handshakes} handshakes! #pwnagotchi #pwnlog #pwnlife #hacktheplanet #skynet').format(
            duration=last_session.duration_human,
            deauthed=last_session.deauthed,
            associated=last_session.associated,
            handshakes=last_session.handshakes)

    def hhmmss(self, count, fmt):
        if count > 1:
            # plural
            if fmt == "h":
                return self._("hours")
            if fmt == "m":
                return self._("minutes")
            if fmt == "s":
                return self._("seconds")
        else:
            # singular
            if fmt == "h":
                return self._("hour")
            if fmt == "m":
                return self._("minute")
            if fmt == "s":
                return self._("second")
        return fmt
