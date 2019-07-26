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

    hitter_at_bats = models.IntegerField(default=0)         # 타석
    hitter_hits = models.IntegerField(default=0)            # 안타
    hitter_doubles = models.IntegerField(default=0)         # 2루타
    hitter_triples = models.IntegerField(default=0)         # 3루타
    hitter_home_runs = models.IntegerField(default=0)       # 홈런
    hitter_runs_scored = models.IntegerField(default=0)     # 득점
    hitter_runs_batted_in = models.IntegerField(default=0)  # 타점
    hitter_bases_on_balls = models.IntegerField(default=0)  # 볼넷
    hitter_hits_by_pitches = models.IntegerField(default=0) # 사구
    hitter_strikes_out = models.IntegerField(default=0)     # 삼진
    hitter_steals = models.IntegerField(default=0)          # 도루
    hitter_sacrifice_fly = models.IntegerField(default=0)   # 희생 플라이
    
    hitter_avg = models.FloatField(default=0)              # 타율
    hitter_obp = models.FloatField(default=0)              # 출루율
    hitter_slg = models.FloatField(default=0)              # 장타율
    hitter_ops = models.FloatField(default=0)              # OPS


class PitcherRecord(models.Model):
    # User 모델과 1 : 1 관계
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    
    pitcher_hit_by_pitch = models.IntegerField(default=0)   # 사구
    pitcher_wild_pitch = models.IntegerField(default=0)     # 폭투
    pitcher_earned_runs = models.IntegerField(default=0)    # 자책점
    pitcher_bases_on_balls = models.IntegerField(default=0) # 볼넷
    pitcher_strike_outs = models.IntegerField(default=0)    # 삼진
    pitcher_holds = models.IntegerField(default=0)          # 홀드
    pitcher_saves = models.IntegerField(default=0)          # 세이브
    pitcher_wins = models.IntegerField(default=0)           # 승리
    pitcher_losses = models.IntegerField(default=0)         # 패배
    pitcher_hits = models.IntegerField(default=0)           # 피안타
    pitcher_home_runs = models.IntegerField(default=0)      # 피홈런
    pitcher_runs = models.IntegerField(default=0)           # 실점
    pitcher_games = models.IntegerField(default=0)          # 경기에 나온 수
    
    pitcher_inning_pitched = models.FloatField(default=0)   # 투구 이닝
    pitcher_earned_run_avg = models.FloatField(default=0)   # 방어율
