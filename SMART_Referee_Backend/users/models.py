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
    back_number = models.IntegerField(blank=True, default=0)
    position = models.CharField(
        max_length=2,
        choices=POSITION_CHOICES,
        default=NONE
    )
    credit = models.IntegerField(default=0)
    
    # PITCHER STAT FIELD
    inning_pitched = models.FloatField(default=0) # 투구 이닝
    earned_run = models.IntegerField(default=0) # 자책점
    win = models.IntegerField(default=0) # 승리
    lose = models.IntegerField(default=0) # 패배
    save = models.IntegerField(default=0) # 세이브
    hold = models.IntegerField(default=0) # 홀드
    strike_out = models.IntegerField(default=0) # 삼진
    hits = models.IntegerField(default=0) # 피안타
    bb = models.IntegerField(default=0) # 볼넷
    
    # HITTER STAT FIELD
    
