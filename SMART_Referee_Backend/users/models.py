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
    name = models.CharField(max_length=20, blank=False)
    team_name = models.CharField(max_length=30, blank=True)
    back_number = models.IntegerField(blank=True, default=0)
    position = models.CharField(
        max_length=2,
        choices=POSITION_CHOICES,
        default=NONE
    )
    credit = models.IntegerField(default=0)
    

class HitterRecord(models.Model):
    # User 모델과 1 : 1 관계
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    at_bats = models.IntegerField(default=0)         # 타석
    hits = models.IntegerField(default=0)            # 안타
    doubles = models.IntegerField(default=0)         # 2루타
    triples = models.IntegerField(default=0)         # 3루타
    home_runs = models.IntegerField(default=0)       # 홈런
    runs_scored = models.IntegerField(default=0)     # 득점
    runs_batted_in = models.IntegerField(default=0)  # 타점
    bases_on_balls = models.IntegerField(default=0)  # 볼넷
    hits_by_pitches = models.IntegerField(default=0) # 사구
    strikes_out = models.IntegerField(default=0)     # 삼진
    steals = models.IntegerField(default=0)          # 도루
    sacrifice_fly = models.IntegerField(default=0)   # 희생 플라이
    
    avg = models.FloatField(default=0)              # 타율
    obp = models.FloatField(default=0)              # 출루율
    slg = models.FloatField(default=0)              # 장타율
    ops = models.FloatField(default=0)              # OPS


class PitcherRecord(models.Model):
    # User 모델과 1 : 1 관계
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    
    hit_by_pitch = models.IntegerField(default=0)   # 사구
    wild_pitch = models.IntegerField(default=0)     # 폭투
    earned_runs = models.IntegerField(default=0)    # 자책점
    bases_on_balls = models.IntegerField(default=0) # 볼넷
    strike_outs = models.IntegerField(default=0)    # 삼진
    holds = models.IntegerField(default=0)          # 홀드
    saves = models.IntegerField(default=0)          # 세이브
    wins = models.IntegerField(default=0)           # 승리
    losses = models.IntegerField(default=0)         # 패배
    hits = models.IntegerField(default=0)           # 피안타
    home_runs = models.IntegerField(default=0)      # 피홈런
    runs = models.IntegerField(default=0)           # 실점
    games = models.IntegerField(default=0)          # 경기에 나온 수
    
    inning_pitched = models.FloatField(default=0)   # 투구 이닝
    earned_run_avg = models.FloatField(default=0)   # 방어율
