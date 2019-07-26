from django.db import models

class Play(models.Model):
    # 시작, 중지, 종료 플래그
    flag = models.IntegerField(blank=False)
    
    # 홈베이스 좌표
    # String으로 저장 후 Json loads해서 사용
    base_coordinate = models.CharField(max_length=200, blank=False)
    
    # 타자 신체 좌표
    # String으로 저장 후 Json loads해서 사용
    hitter_coordinate = models.CharField(max_length=200, blank=False)
    
    # 게임 코드를 저장할 필드
    game_code = models.CharField(max_length=10)
    
    # 시간 관련 필드
    # auto_now_add, auto_add 는 추가로 생각해서 구성
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    pause_start_at = models.DateField()
    pause_end_at = models.DateField()
