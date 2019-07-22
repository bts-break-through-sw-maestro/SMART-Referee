from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    PITCHER = 'P'
    CATCHER = 'C'
    FIRSTBASE = '1B'
    SECONDBASE = '2B'
    THIRDBASE = '3B'
    SHORTSTOP = 'SS'
    LEFTFIELD = 'LF'
    CENTERFIELD = 'CF'
    RIGHTFIELD = 'RF'
    DESIGNATEDHITTER = 'DH'
    NONE = 'NN'
    
    POSITION_CHOICES = [
        (PITCHER, 'Pitcher'),
        (CATCHER, 'Catcher'),
        (FIRSTBASE, 'First Base'),
        (SECONDBASE, 'Second Base'),
        (THIRDBASE, 'Third Base'),
        (SHORTSTOP, 'Short Stop'),
        (LEFTFIELD, 'Left Field'),
        (CENTERFIELD, 'Center Field'),
        (RIGHTFIELD, 'Right Field'),
        (DESIGNATEDHITTER, 'Designated Hitter'),
        (NONE, 'None'),
    ]
    
    # Djano의 User 모델과 1 : 1 관계
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # PLAYER STAT FIELD
    # team_name : 팀명    # back_number : 등번호  
    # position  : 포지션  # credit      : 코인    
    team_name = models.CharField(max_length=30, blank=True)
    back_number = models.PositiveIntegerField(blank=False, default=0)
    position = models.CharField(
        max_length=2,
        choices=POSITION_CHOICES,
        default=NONE
    )
    credit = models.PositiveIntegerField(default=0)
    
    # PITCHER STAT FIELD
    # era       : 방어율  # speed : 평균 구속  
    # strikeout : 탈삼진  # win   : 승리
    # lose      : 패배    # save  : 세이브
    era = models.FloatField(blank=True)
    speed = models.FloatField(blank=True)
    strikeout = models.PositiveIntegerField(blank=True)
    win = models.PositiveIntegerField(blank=True)
    lose = models.PositiveIntegerField(blank=True)
    save = models.PositiveIntegerField(blank=True)
    
    # HITTER STAT FIELD
    # avg : 타율    # obp   : 출루율
    # slg : 장타율  # ops   : OPS
    # rbi : 타점    # steal : 도루
    avg = models.FloatField(blank=True, default=0)
    obp = models.FloatField(blank=True)
    slg = models.FloatField(blank=True)
    ops = models.FloatField(blank=True)
    rbi = models.PositiveIntegerField(blank=True)
    steal = models.PositiveIntegerField(blank=True)
