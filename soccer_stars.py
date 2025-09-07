import pygame , random , math ,time
pygame.init() 
pygame.mixer.init()
goal_font = pygame.font.Font(None, 200)
font = pygame.font.Font(None, 150)
font1 = pygame.font.Font(None, 500) 
disp=pygame.display.set_mode((1000,600)) 
# Images  
menu_image=pygame.image.load('pictures/menu.jpeg')  
menu_image=pygame.transform.scale(menu_image,(1000,600))  
setting_image=pygame.image.load('pictures/setting_menu.jpg')
setting_image=pygame.transform.scale(setting_image,(1000,600))
setting_ground_image=pygame.image.load('pictures/setting_ground.jpg')
setting_ground_image=pygame.transform.scale(setting_ground_image,(1000,600))
ground_image=pygame.image.load('pictures/groundempty.png')  
ground_image=pygame.transform.scale(ground_image,(1000,600))  
loading_image=pygame.image.load('pictures/loading.jpg')  
loading_image=pygame.transform.scale(loading_image,(1000,600))  
form_bot_image=pygame.image.load('pictures/loading formbot.png')  
form_bot_image=pygame.transform.scale(form_bot_image,(800,450))  
form1_image=pygame.image.load('pictures/loading form1.png')  
form1_image=pygame.transform.scale(form1_image,(800,450))  
form2_image=pygame.image.load('pictures/loading form2.png')  
form2_image = pygame.transform.scale(form2_image,(800,450))  
random_image=pygame.image.load('pictures/random.png')  
random_image = pygame.transform.scale(random_image,(165,70))  
single_image=pygame.image.load('pictures/single.png')  
single_image = pygame.transform.scale(single_image,(130,120))  
two_image=pygame.image.load('pictures/two.png')  
two_image = pygame.transform.scale(two_image,(130,120))  
setting_image2=pygame.image.load('pictures/settings.png')  
setting_image2 = pygame.transform.scale(setting_image2,(70,78))  
form2_image=pygame.image.load('pictures/loading form2.png')  
form2_image = pygame.transform.scale(form2_image,(800,450))  
playerb_image=pygame.image.load('pictures/player blue.png')  
playerb_image=pygame.transform.scale(playerb_image,(57,70))  
playerr_image=pygame.image.load('pictures/player red.png')  
playerr_image=pygame.transform.scale(playerr_image,(57,70))  
ball_image=pygame.image.load('pictures/ball.png')  
ball_image=pygame.transform.scale(ball_image,(27,32))  
t113_image=pygame.image.load('pictures/tactics/113.png')  
t113_image=pygame.transform.scale(t113_image,(175,300))  
t113_imageb=pygame.transform.scale(t113_image,(190,310))  
t221_image=pygame.image.load('pictures/tactics/221.png')  
t221_image=pygame.transform.scale(t221_image,(175,300))  
t221_imageb=pygame.transform.scale(t221_image,(190,310)) 
t230_image=pygame.image.load('pictures/tactics/230.png')  
t230_image=pygame.transform.scale(t230_image,(175,300))  
t230_imageb=pygame.transform.scale(t230_image,(190,310))  
t320_image=pygame.image.load('pictures/tactics/320.png')  
t320_image=pygame.transform.scale(t320_image,(175,300))
t320_imageb=pygame.transform.scale(t320_image,(190,310))
goal1=pygame.image.load('pictures/goal1.png')
goal1=pygame.transform.scale(goal1,(50,200)) 
goal2=pygame.image.load('pictures/goal2.png')  
goal2=pygame.transform.scale(goal2,(50,200))  
txt1=pygame.image.load('pictures/player1.png')
txt1=pygame.transform.scale(txt1,(100,30))
txt2=pygame.image.load('pictures/player2.png')
txt2=pygame.transform.scale(txt2,(100,30))
# Sounds
all_sound = pygame.mixer.music.load('sounds/all 3.mp3')
start_sound = pygame.mixer.Sound('sounds/start_sot.mp3')
player_sound = pygame.mixer.Sound('sounds/player.mp3')
player_wall_sound = pygame.mixer.Sound('sounds/wall.mp3')
goal_sound = pygame.mixer.Sound('sounds/goal.mp3')
end_sound = pygame.mixer.Sound('sounds/end.mp3')
click_sound = pygame.mixer.Sound('sounds/click.mp3')
# Defs
def loader():
    disp.blit(loading_image,(0,0))
    num_dots=len(loading_dots)
    for i in range(num_dots):
      index=(loading+i)%num_dots
      size=5+i
      color=(255-(i*15),255-(i*15),255-(i*15))
      pygame.draw.circle(disp,color,loading_dots[index],size)
def tactic_selection():
    disp.blit(loading_image,(0,0))
    image=form1_image
    if game_state==2:
      if game_type=="single":
        image=form_bot_image
      else:
        image=form2_image
    disp.blit(image,(100,130))
    disp.blit(t113_image,(120,265))  
    disp.blit(t221_image,(315,265))  
    disp.blit(t230_image,(510,265))  
    disp.blit(t320_image,(705,265)) 
def create_object(x, y, radius, image):
    return {'x': x, 'y': y, 'radius': radius, 'image': image, 'vel_x': 0, 'vel_y': 0}
def draw_object(obj):
    disp.blit(obj['image'], (obj['x'] - obj['radius'], obj['y'] - obj['radius']))
def move_object(obj):
    obj['x'] += obj['vel_x']
    obj['y'] += obj['vel_y']
    obj['vel_x'] *= 0.98
    obj['vel_y'] *= 0.98
    if abs(obj['vel_x']) < 0.1: obj['vel_x'] = 0
    if abs(obj['vel_y']) < 0.1: obj['vel_y'] = 0
    hit=False
    if obj['x'] - obj['radius'] <= 85 and not (260 <= obj['y'] <= 440):
        obj['x'] = 85 + obj['radius']
        obj['vel_x'] = -obj['vel_x']
        hit=True
    elif obj['x'] + obj['radius'] >= 915 and not (260 <= obj['y'] <= 440):
        obj['x'] = 915 - obj['radius']
        obj['vel_x'] = -obj['vel_x']
        hit=True
    if obj['x'] - obj['radius'] <= 50 and  (260 <= obj['y'] <= 440):
        obj['x'] = 85 + obj['radius']
        obj['vel_x'] = -obj['vel_x']
        hit=True
    elif obj['x'] + obj['radius'] >= 960 and  (260 <= obj['y'] <= 440):
        obj['x'] = 915 - obj['radius']
        obj['vel_x'] = -obj['vel_x']
        hit=True
    if obj['y'] - obj['radius'] <= 103:
        obj['y'] = 103 + obj['radius']
        obj['vel_y'] = -obj['vel_y']
        hit=True
    elif obj['y'] + obj['radius'] >= 585:
        obj['y'] = 585 - obj['radius']
        obj['vel_y'] = -obj['vel_y']
        hit=True
    if hit:
        player_wall_sound.play()
def check_collision(obj1, obj2):
    dx = obj1['x'] - obj2['x']
    dy = obj1['y'] - obj2['y']
    distance = math.hypot(dx, dy)
    if distance < obj1['radius'] + obj2['radius']:
        player_sound.play()
        angle = math.atan2(dy, dx)
        if obj1['radius'] > obj2['radius']:
            m1, m2 = 20, 4
        elif obj1['radius'] < obj2['radius']:
            m1, m2 = 4, 20
        else:
            m1, m2 = 20, 20
        v1 = obj1['vel_x'] * math.cos(angle) + obj1['vel_y'] * math.sin(angle)
        v2 = obj2['vel_x'] * math.cos(angle) + obj2['vel_y'] * math.sin(angle)
        v1_final = (v1 * (m1 - m2) + 2 * m2 * v2) / (m1 + m2*2)
        v2_final = (v2 * (m2 - m1) + 2 * m1 * v1) / (m1 + m2)
        obj1['vel_x'] += (v1_final - v1) * math.cos(angle)
        obj1['vel_y'] += (v1_final - v1) * math.sin(angle)
        obj2['vel_x'] += (v2_final - v2) * math.cos(angle)
        obj2['vel_y'] += (v2_final - v2) * math.sin(angle)
        overlap = obj1['radius'] + obj2['radius'] - distance
        obj1['x'] += math.cos(angle) * (overlap / 2)
        obj1['y'] += math.sin(angle) * (overlap / 2)
        obj2['x'] -= math.cos(angle) * (overlap / 2)
        obj2['y'] -= math.sin(angle) * (overlap / 2)
def is_moving(objs):
    for obj in objs:
        if obj['vel_x'] != 0 or obj['vel_y'] != 0:
            return True
    return False
def bot_turn():
    global turn, selected_piece
    if turn != 1:
        return
    bot_pieces = players[5:]
    opp_pieces = players[:5]
    best_piece = None
    best_score = float('-inf')
    for piece in bot_pieces:
        dx = ball['x'] - piece['x']
        dy = ball['y'] - piece['y']
        dist_to_ball = math.hypot(dx, dy)
        if dist_to_ball == 0:
            continue  
        looking_forward = dx > 0
        score = -dist_to_ball
        if looking_forward:
            score += 50
        for opp in opp_pieces:
            opp_dist = math.hypot(opp['x'] - piece['x'], opp['y'] - piece['y'])
            ball_dist = dist_to_ball
            if opp_dist < ball_dist and math.hypot(opp['x'] - ball['x'], opp['y'] - ball['y']) < 50:
                score -= 100
                break
        if score > best_score:
            best_score = score
            best_piece = piece
    if not best_piece:
        min_dist = float('inf')
        for piece in bot_pieces:
            dist = math.hypot(piece['x'] - ball['x'], piece['y'] - ball['y'])
            if dist < min_dist:
                min_dist = dist
                best_piece = piece
    if best_piece:
        dx = ball['x'] - best_piece['x']
        dy = ball['y'] - best_piece['y']
        dist = math.hypot(dx, dy)
        if dist == 0:
            dx, dy = 1, 0 
            dist = 1
        power = min(12, dist * 0.2)
        best_piece['vel_x'] = dx / dist * power
        best_piece['vel_y'] = dy / dist * power
        turn = 0
def check_goal(ball,r):
    if 50 <= ball['x'] <= 70 and 263 <= ball['y'] <= 437:
        ball['x'] = 60
        ball['vel_x'] = 0
        ball['vel_y'] = 0
        show_goal_effect("red",r+1)
        time.sleep(2)
        return 'red'
    if 930 <= ball['x'] <= 960 and 263 <= ball['y'] <= 437:
        ball['x'] = 950
        ball['vel_x'] = 0
        ball['vel_y'] = 0
        show_goal_effect("blue",r+1)
        time.sleep(2)
        return 'blue'
    return None
def show_goal_effect(winner,r):
    text = goal_font.render("GOAL!", True, (255, 215, 0))
    if winner == "blue" :
        if r==3:
            winr = font.render("Blue Winer", True, (0, 0, 255)) 
            disp.blit(winr,(300,200))
            end_sound.play()
        else:
            scorer = font.render("goooooal", True, (0, 0, 255))
            disp.blit(scorer, (300, 350))
            disp.blit(text, (300, 200))
            goal_sound.play()
    else:
        if r==3:
            winr = font.render("Red Winer", True, (255, 0, 0)) 
            disp.blit(winr,(300,200))
            end_sound.play()
        else:
            scorer = font.render("goooooal", True, (255, 0, 0))
            disp.blit(scorer, (300, 350))
            disp.blit(text, (300, 200))
            goal_sound.play()
    disp.blit(goal1, (38, 236)) 
    disp.blit(goal2, (910, 236)) 
    pygame.display.update()
    pygame.time.delay(2000)
a=False
run=True
while run:
    if not a:
        v = 0.5
        pygame.mixer.music.set_volume(v)
        pygame.mixer.music.play(-1)
        tactics = [  
            [[340,400],[340,260],[130,330],[230,330],[410,330]],[[660,400],[660,260],[870,330],[770,330],[590,330]],  
            [[165,400],[165,280],[120,240],[120,440],[200,340]],[[835,400],[835,280],[880,240],[880,440],[800,340]],  
            [[195,265],[195,425],[120,265],[120,425],[195,345]],[[805,265],[805,425],[880,265],[880,425],[805,345]],  
            [[140,415],[140,345],[140,275],[200,305],[200,380]],[[860,415],[860,345],[860,275],[800,305],[800,380]]  
        ]  
        select_tactic = [  
            ["t113",120,265,175,300,0],  
            ["t221",315,265,175,300,2],  
            ["t230",510,265,175,300,4],  
            ["t320",705,265,175,300,6]  
        ]  
        loading_dots=[(500,420),(540,430),(570,460),(580,500),(570,540),(540,565),(500,570),(465,565),(435,540),(420,500),(430,460),(460,430)]  
        game_state=0
        gs=0
        player1_tactic=None  
        player2_tactic=None 
        select_player = None
        game_type='' 
        setting_menu = [515,410]
        single_player=[360,470,430,580] 
        two_player=[600,470,710,580]
        ball = [485,330]
        player_turn = 'b'
        n = 1
        t=0
        x1=198
        y1=691
        done = False  
        loading = 0
        disp.fill((0,0,0)) 
        while not done:  
            # Event  
            for event in pygame.event.get():  
                if event.type==pygame.QUIT:  
                    done = True  
                    run=False
                    pygame.quit()
                if event.type==pygame.MOUSEBUTTONDOWN:  
                    (x,y)=event.pos
                    if game_state==3:
                        for i in range(len(select_tactic)):  
                            if select_tactic[i][1]<= x <=select_tactic[i][1]+select_tactic[i][3] and 265 <= y <= 565:
                                click_sound.play()           
                                disp.blit(t113_imageb if i==0 else t221_imageb if i==1 else t230_imageb if i==2 else t320_imageb,(select_tactic[i][1]-10,259))
                                pygame.display.update()  
                                time.sleep(0.3)
                                player2_tactic=select_tactic[i][5]  
                                game_state=4
                        if 750<= x <=950 and 180<= y <=240: 
                            click_sound.play()
                            disp.blit(random_image,(716,174))
                            pygame.display.update()  
                            time.sleep(0.3)
                            player2_tactic=select_tactic[random.randint(0,len(select_tactic)-1)][5]  
                            game_state=4
                    if game_state==2: 
                        for i in range(len(select_tactic)):  
                            if select_tactic[i][1]<= x <=select_tactic[i][1]+select_tactic[i][3] and 265 <= y <= 565:
                                click_sound.play()
                                disp.blit(t113_imageb if i==0 else t221_imageb if i==1 else t230_imageb if i==2 else t320_imageb,(select_tactic[i][1]-10,259))
                                pygame.display.update()  
                                time.sleep(0.3)
                                player1_tactic=select_tactic[i][5]  
                                game_state=3   
                        if 720<= x <=875 and 180<= y <=240:
                            click_sound.play()
                            disp.blit(random_image,(716,174))
                            pygame.display.update()  
                            time.sleep(0.3)
                            player1_tactic=select_tactic[random.randint(0,len(select_tactic)-1)][5]  
                            game_state=3 
                    if game_state==0:
                        if  485 <= x <= 545 and 380 <= y <= 440 :
                            click_sound.play()
                            gs=game_state
                            game_state = -1
                            disp.blit(setting_image2,(479,372))
                            pygame.display.update()  
                            time.sleep(0.3)
                            disp.blit(menu_image,(0,0))
                            pygame.display.update() 
                            time.sleep(0.1)
                        if single_player[0]<= x <=single_player[2] and single_player[1]<= y <=single_player[3]:  
                            click_sound.play()
                            game_type='single'  
                            game_state=1
                            disp.blit(single_image,(303,468))
                            pygame.display.update()  
                            time.sleep(0.3)
                            disp.blit(menu_image,(0,0))
                            pygame.display.update() 
                            time.sleep(0.1)
                        elif two_player[0]<= x <=two_player[2] and two_player[1]<= y <=two_player[3]:  
                            click_sound.play()
                            game_type='two'  
                            game_state=1
                            disp.blit(two_image,(590,468))
                            pygame.display.update()  
                            time.sleep(0.3)
                            disp.blit(menu_image,(0,0))
                            pygame.display.update() 
                            time.sleep(0.1)
                        c = pygame.time.get_ticks()
                    if game_state == -2 :
                        if 370 <= x <= 630 and 375 <= y <= 445 :
                            click_sound.play()
                            done = True
                            run = False
                        if 370 <= x <= 630 and 290 <= y <=360 :
                            click_sound.play()
                            game_state = gs
                            gs=0
                        if 405 <= x <= 445 and 210 <= y <= 250 :
                            v -= 0.1
                            pygame.mixer.music.set_volume(v)
                        if 553 <= x <= 593 and 210 <= y <= 250 :
                            v += 0.1
                            pygame.mixer.music.set_volume(v)                           
            if game_state==-1 :
                disp.blit(setting_image,(0,0))
                game_state = -2
            if game_state==0: 
                disp.blit(menu_image,(0,0))
            elif game_state==1: 
                if (pygame.time.get_ticks()-c)>=2000:  
                    tactic_selection()  
                    game_state=2
                else:  
                    loader()  
                    loading=(loading+1)%len(loading_dots)  
            elif game_state == 3:
                tactic_selection()  
            elif game_state == 4: 
                if n == 1 :
                    start_sound.play()
                a=True
                done=True
            pygame.display.update()  
            pygame.time.Clock().tick(30) 
    if a:
        clock = pygame.time.Clock()
        players = [
            create_object(tactics[player1_tactic][0][0],tactics[player1_tactic][0][1], 28, playerb_image),
            create_object(tactics[player1_tactic][1][0],tactics[player1_tactic][1][1], 28, playerb_image),
            create_object(tactics[player1_tactic][2][0],tactics[player1_tactic][2][1], 28, playerb_image),
            create_object(tactics[player1_tactic][3][0],tactics[player1_tactic][3][1], 28, playerb_image),
            create_object(tactics[player1_tactic][4][0],tactics[player1_tactic][4][1], 28, playerb_image),
            create_object(tactics[player2_tactic+1][0][0],tactics[player2_tactic+1][0][1], 28, playerr_image),
            create_object(tactics[player2_tactic+1][1][0],tactics[player2_tactic+1][1][1], 28, playerr_image),
            create_object(tactics[player2_tactic+1][2][0],tactics[player2_tactic+1][2][1], 28, playerr_image),
            create_object(tactics[player2_tactic+1][3][0],tactics[player2_tactic+1][3][1], 28, playerr_image),
            create_object(tactics[player2_tactic+1][4][0],tactics[player2_tactic+1][4][1], 28, playerr_image),
        ]
        ball = create_object(500, 345, 16, ball_image)
        selected_piece = None
        turn = 0
        dragging = False
        running = True
        blue_score=0
        red_score=0
        blue_s = font.render(str(blue_score), True, (255, 255, 255))
        red_s = font.render(str(red_score), True, (255, 255, 255))
        setting=False
        g=0
        while running:
                disp.blit(ground_image, (0, 0))
                disp.blit(playerb_image,(30,10)) 
                disp.blit(playerr_image,(920,10))  
                disp.blit(txt1,(100,10))  
                disp.blit(txt2,(790,10)) 
                blue_s = font.render(str(blue_score), True, (255, 255, 255))
                red_s = font.render(str(red_score), True, (255, 255, 255)) 
                disp.blit(blue_s,(340,5))
                disp.blit(red_s,(610,5))
                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT:
                        a=False
                        running = False 
                    if event.type == pygame.MOUSEBUTTONDOWN:  
                        if not is_moving(players + [ball]): 
                            x, y = event.pos 
                            for i, player in enumerate(players):
                                if (turn == 0 and i < 5) or (turn == 1 and i >= 5): 
                                    if math.hypot(x - player['x'], y - player['y']) < player['radius']:
                                        selected_piece = player
                                        dragging = True
                                        break
                    if event.type == pygame.MOUSEBUTTONUP and selected_piece:
                        x, y = event.pos
                        dx = selected_piece['x'] - x
                        dy = selected_piece['y'] - y
                        distance = math.hypot(dx, dy)
                        max_power = 20
                        if distance > 150:
                            dx = dx / distance * 150
                            dy = dy / distance * 150
                        selected_piece['vel_x'] = dx * 0.09
                        selected_piece['vel_y'] = dy * 0.09
                        selected_piece = None
                        dragging = False
                        turn = 1 - turn
                    if event.type == pygame.MOUSEMOTION:
                        mouse_pos = event.pos
                for player in players:
                    move_object(player)
                    check_collision(player, ball)
                move_object(ball)
                for i in range(len(players)):
                    for j in range(i + 1, len(players)):
                        check_collision(players[i], players[j])
                goal = check_goal(ball,red_score)
                if goal=="red":
                    red_score+=1
                    if red_score==3:
                        a=False
                        running =False
                    turn=0
                if goal == "blue":
                    blue_score+=1
                    if blue_score==3:
                        time.sleep(3) 
                        a=False
                        running=False
                    turn=1
                if goal and blue_score<3 and red_score<3:
                    ball = create_object(500, 345, 16, ball_image)
                    players = [
                        create_object(tactics[player1_tactic][0][0], tactics[player1_tactic][0][1], 28, playerb_image),
                        create_object(tactics[player1_tactic][1][0], tactics[player1_tactic][1][1], 28, playerb_image),
                        create_object(tactics[player1_tactic][2][0], tactics[player1_tactic][2][1], 28, playerb_image),
                        create_object(tactics[player1_tactic][3][0], tactics[player1_tactic][3][1], 28, playerb_image),
                        create_object(tactics[player1_tactic][4][0], tactics[player1_tactic][4][1], 28, playerb_image),
                        create_object(tactics[player2_tactic+1][0][0], tactics[player2_tactic+1][0][1], 28, playerr_image),
                        create_object(tactics[player2_tactic+1][1][0], tactics[player2_tactic+1][1][1], 28, playerr_image),
                        create_object(tactics[player2_tactic+1][2][0], tactics[player2_tactic+1][2][1], 28, playerr_image),
                        create_object(tactics[player2_tactic+1][3][0], tactics[player2_tactic+1][3][1], 28, playerr_image),
                        create_object(tactics[player2_tactic+1][4][0], tactics[player2_tactic+1][4][1], 28, playerr_image),
                    ]
                    selected_piece = None
                    start_sound.play()
                    pygame.time.delay(1000)
                for player in players:
                    draw_object(player)
                draw_object(ball)
                if selected_piece and dragging:
                    x1, y1 = selected_piece['x'], selected_piece['y']
                    x2, y2 = mouse_pos
                    dx, dy = x1 - x2, y1 - y2
                    distance = math.hypot(dx, dy)
                    max_length = 100
                    if distance > max_length:
                        dx = dx / distance * max_length
                        dy = dy / distance * max_length
                    pygame.draw.line(disp, (255, 255, 0), (x1, y1), (x1 - dx, y1 - dy), 3)
                def all_stopped():
                    objs = players + [ball]
                    return all(abs(o['vel_x']) < 0.1 and abs(o['vel_y']) < 0.1 for o in objs)
                if all_stopped() and game_type=="single":
                    bot_turn()
                disp.blit(goal1, (38, 236)) 
                disp.blit(goal2, (910, 236)) 
                pygame.display.update()  
                clock.tick(60)  
pygame.quit()