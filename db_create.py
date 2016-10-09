from project import db
import os

from project.home.models import *

db.drop_all()
db.create_all()
handles = ['BarackObama','JoeBiden','SpeakerRyan','MittRomney','Schwarzenegger','QueenRania','CoryBooker','ShashiTharoor','RoyalCentral','NicolasSarkozy','newtgingrich','SenJohnMcCain','Voting4Romney','GovGaryJohnson','SarahPalinUSA','alfranken','NelsonMandela','GovMikeHuckabee','joseserra_','THEHermanCain','algore','RickSantorum','MrKRudd','JonHuntsman','GovernorPerry','GavinNewsom','SenatorBoxer','JerryBrownGov','MicheleBachmann','GabbyGiffords','fidelcastro','ThadMcCotter','TimPawlenty','DanaPerino','billclinton','GEJonathan','MarkNeumann05','ScottBrown8','BuddyRoemer','RonPaul','SarahBrownUK','MegWhitman','hatoyama_y_en','chavezcandanga']

for handle in handles:
    db.session.add(Figure(handle, None))

db.session.commit()

