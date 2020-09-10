#__author__ = "Prateek Rawat"
#!usr/bin/python

from pydub import AudioSegment
from pydub.playback import play

backSound = AudioSegment.from_mp3("other/backSound.mp3")

audioDict = {
	"kripya": "other/kripya.mp3",
	"pehle": "other/pehle.mp3",
	"lagaye": "other/lagaye.mp3",
	"apna": "other/apna.mp3",
	"angootha": "other/thumb.mp3",
	"liya": "other/liya.mp3",
	"apne": "other/apne.mp3",
	"apka": "other/apka.mp3",
	"ungali": "other/ungali.mp3",
	"gehu": "other/gehu.mp3",
	"dal": "other/dal.mp3",
	"chaval": "other/chaval.mp3",
	"bill": "other/bill.mp3",
	"hai": "other/hai.mp3",
	"aapne": "other/aapne.mp3",
	"apni": "other/apni.mp3",
	"baad": "other/baad.mp3",
	"baat": "other/baat.mp3",
	"bahut": "other/bahut.mp3",
	"battery": "other/battery.mp3",
	"chayan": "other/chayan.mp3",
	"dushamlev": "other/dushamlev.mp3",
	"gaya": "other/gaya.mp3",
	"haan": "other/haan.mp3",
	"hain": "other/hain.mp3",
	"hazar": "other/hazar.mp3",
	"hota": "other/hota.mp3",
	"hua": "other/hua.mp3",
	"hue": "other/hue.mp3",
	"hui": "other/hui.mp3",
	"ka": "other/ka.mp3",
	"len_den": "other/len_den.mp3",
	"safal": "other/safal.mp3",
	"scanning": "other/scanning.mp3",
	"vastuoo": "other/vastuoo.mp3",
	"rakhe": "other/rkhe.mp3",
	"liye": "other/liye.mp3",
	"kul": "other/kul.mp3",
	"lagat": "other/lagat.mp3",
	"so": "other/so.mp3",
	"paise": "other/paise.mp3",
	"aapne": "other/aapne.mp3"
}

numberDict = {
	"1": "numbers/1.mp3",
	"2": "numbers/2.mp3",
	"3": "numbers/3.mp3",
	"4": "numbers/4.mp3",
	"5": "numbers/5.mp3",
	"6": "numbers/6.mp3",
	"7": "numbers/7.mp3",
	"8": "numbers/8.mp3",
	"9": "numbers/9.mp3",
	"10": "numbers/10.mp3",
	"11": "numbers/11.mp3",
	"12": "numbers/12.mp3",
	"13": "numbers/13.mp3",
	"14": "numbers/14.mp3",
	"15": "numbers/15.mp3",
	"16": "numbers/16.mp3",
	"17": "numbers/17.mp3",
	"18": "numbers/18.mp3",
	"19": "numbers/19.mp3",
	"20": "numbers/20.mp3",
	"21": "numbers/21.mp3",
	"22": "numbers/22.mp3",
	"23": "numbers/23.mp3",
	"24": "numbers/24.mp3",
	"25": "numbers/25.mp3",
	"26": "numbers/26.mp3",
	"27": "numbers/27.mp3",
	"28": "numbers/28.mp3",
	"29": "numbers/29.mp3",
	"30": "numbers/30.mp3",
	"31": "numbers/31.mp3",
	"32": "numbers/32.mp3",
	"33": "numbers/33.mp3",
	"34": "numbers/34.mp3",
	"35": "numbers/35.mp3",
	"36": "numbers/36.mp3",
	"37": "numbers/37.mp3",
	"38": "numbers/38.mp3",
	"39": "numbers/39.mp3",
	"40": "numbers/40.mp3",
	"41": "numbers/41.mp3",
	"42": "numbers/42.mp3",
	"43": "numbers/43.mp3",
	"44": "numbers/44.mp3",
	"45": "numbers/45.mp3",
	"46": "numbers/46.mp3",
	"47": "numbers/47.mp3",
	"48": "numbers/48.mp3",
	"49": "numbers/49.mp3",
	"50": "numbers/50.mp3",
	"51": "numbers/51.mp3",
	"52": "numbers/52.mp3",
	"53": "numbers/53.mp3",
	"54": "numbers/54.mp3",
	"55": "numbers/55.mp3",
	"56": "numbers/56.mp3",
	"57": "numbers/57.mp3",
	"58": "numbers/58.mp3",
	"59": "numbers/59.mp3",
	"60": "numbers/60.mp3",
	"61": "numbers/61.mp3",
	"62": "numbers/62.mp3",
	"63": "numbers/63.mp3",
	"64": "numbers/64.mp3",
	"65": "numbers/65.mp3",
	"66": "numbers/66.mp3",
	"67": "numbers/67.mp3",
	"68": "numbers/68.mp3",
	"69": "numbers/69.mp3",
	"70": "numbers/70.mp3",
	"71": "numbers/71.mp3",
	"72": "numbers/72.mp3",
	"73": "numbers/73.mp3"
}

#function to normalize all merged audios
def match_target_amplitude(sound, target_dBFS):
	change_in_dBFS = target_dBFS - sound.dBFS
	return sound.apply_gain(change_in_dBFS)


#function to change speed of dictation
def speed_change(sound, speed=1.0):
    # Manually override the frame_rate. This tells the computer how many
    # samples to play per second
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
         "frame_rate": int(sound.frame_rate * speed)
      })
     # convert the sound with altered frame rate to a standard frame rate
     # so that regular playback programs will work right. They often only
     # know how to play audio at standard frame rate (like 44.1k)
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

print("\n\n\n\n*******ALLOWED WORDS********\n")

allowed_words = list(audioDict)
for words in allowed_words:
	print(words, end = " ")
print("\n\n\nAllowed numbers: 0-73")

final = AudioSegment.empty()
sentence = input("\n\n\nEnter Text: ?\b")
#sentence = "kripya pehle apna angootha lagaye"

try:
	for words in sentence.split():
		if words.isnumeric():
			speech = AudioSegment.from_mp3(numberDict.get(words))
		else:
			speech = AudioSegment.from_mp3(audioDict.get(words))
except (AttributeError):
	print("Word doesn't exist in the database! Use valid words.")
except:
	print('[ERROR] Unknown error encountered!')
	raise
else:
	for words in sentence.split():
		if words.isnumeric():
			speech = AudioSegment.from_mp3(numberDict.get(words))
		else:
			speech = AudioSegment.from_mp3(audioDict.get(words))
		final += speech
	
normalized_audio = match_target_amplitude(final, -10.0)  #final.export("final.wav", format ="wav")
#frame_rate_audio = normalized_audio.getframerate()
#normalized_audio.setframerate(2*frame_rate_audio)

#add background sound to make it sound more natural
sound2 = normalized_audio.overlay(backSound, loop=True)

#increase speed to remove the pauses and make the sound more natural
sound3 = speed_change(sound2, 1.0)
play(sound3)