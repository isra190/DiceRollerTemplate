# put your dice_roll() function in this file
import random

def roll_dice(type_d):
    dice_range = range(1, type_d + 1)
    face_value = random.choice(dice_range)
    return face_value


from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

die_faces = {
    "4": '<svg width="50" height="50"><polygon points="0,3 25,46 50,3" style="stroke: black; fill: none" /><text fill="black" x="20" y="26" font-family="Verdana" font-size="18">REPLACEMENT</text></svg>',
    "6": '<svg width="50" height="50"><polygon points="3,3 3,47 47,47 47,3" style="stroke: black; fill: none" /><text fill="black" x="20" y="30" font-family="Verdana" font-size="18">REPLACEMENT</text></svg>',
    "8": '<svg width="60" height="50"><polygon points="17,0 60,25 17,50 17,0 0,25 17,50" style="stroke: black; fill: none" /><text fill="black" x="25" y="30" font-family="Verdana" font-size="18">REPLACEMENT</text></svg>',
    "10": '<svg width="50" height="50"><polygon points="43,50 0,25 43,0 50,25" style="stroke: black; fill: none" /><text fill="black" x="20" y="30" font-family="Verdana" font-size="18">REPLACEMENT</text></svg>',
    "12": '<svg width="50" height="50"><polygon points="25,0 1,17 10,45 40,45 49,17" style="stroke: black; fill: none" /><text fill="black" x="13" y="30" font-family="Verdana" font-size="18">REPLACEMENT</text></svg>',
    "20": '<svg width="50" height="50"><polygon points="0,46 25,0 50,46" style="stroke: black; fill: none" /><text fill="black" x="13" y="40" font-family="Verdana" font-size="18">REPLACEMENT</text></svg>',
    "other": '<svg width="50" height="50"><circle cx="25" cy="25" r="20" style="stroke: black; fill: none" /><text fill="black" x="13" y="31" font-family="Verdana" font-size="18">REPLACEMENT</text></svg>'
}
