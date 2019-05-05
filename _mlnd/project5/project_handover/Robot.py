import random

class Robot(object):

    def __init__(self, maze, alpha=0.5, gamma=0.9, epsilon0=0.5):

        self.maze = maze
        ## 继承生成的maze
        self.valid_actions = self.maze.valid_actions
        ## 继承maze中的动作
        self.state = None
        self.action = None

        # Set Parameters of the Learning Robot
        self.alpha = alpha
        ## alpha是学习率，就是新结果更新到Q-Table的比率
        self.gamma = gamma
        ##  gamma是对未来奖励的惩罚
        self.epsilon0 = epsilon0
        self.epsilon = epsilon0
        ## epsilon是贪婪算法的随机率
        ## 初始值为 epsilon0
        self.t = 0
        ## epsilon 更新的次数

        self.Qtable = {}
        ## 初始化空的Qtable
        self.reset()

    def reset(self):
        """
        Reset the robot
        """
        self.state = self.sense_state()
        self.create_Qtable_line(self.state)

    def set_status(self, learning=False, testing=False):
    ## 设定 learning 和 testing 两种过程状态参数
        """
        Determine whether the robot is learning its q table, or
        exceuting the testing procedure.
        """
        self.learning = learning
        self.testing = testing

    def update_parameter(self):
        """
        Some of the paramters of the q learning robot can be altered,
        update these parameters when necessary.
        """
        if self.testing:
            # TODO 1. No random choice when testing
            ## 如果是 testing 的参数是 True，不更新 epsilon
            ## 直接pass
            pass
        else:
            # TODO 2. Update parameters when learning
            self.t = self.t +1
            ## t的记数加1
            if self.epsilon < 0.025:
                self.epsilon = self.epsilon - self.t*0.2
                ## 当 epsilon 比较小的时候，Qtable接近完美值
                ## 增加衰减，迅速减少随机探索比率
            else:
                self.epsilon = self.epsilon - self.t*0.1
                ## 当 epsilon 在 epsilon0 和 0.25 之间，Qtable还比较不完善
                ## 保持比较低的衰减，缓速减少随机探索比率
        return self.epsilon

    def sense_state(self):
        """
        Get the current state of the robot. In this
        """

        # TODO 3. Return robot's current state
        return self.maze.sense_robot()
        # 获得机器人位置

    def create_Qtable_line(self, state):
        """
        Create the qtable with the current state
        """
        # TODO 4. Create qtable with current state
        # Our qtable should be a two level dict,
        # Qtable[state] ={'u':xx, 'd':xx, ...}
        # If Qtable[state] already exits, then do
        # not change it.
        if state in self.Qtable:  
        # Qtable是字典，调用字典的键值查找属性，如果有，什么都不做
            pass
        else:
            self.Qtable[state] = {'u':0.0, 'r':0.0, 'd':0.0, 'l':0.0} 
            # 没有的话，新增一个状态，赋值为0.0(float)

    def choose_action(self):
        """
        Return an action according to given rules
        """
        def is_random_exploration():

            # TODO 5. Return whether do random choice
            # hint: generate a random number, and compare
            # it with epsilon
            return np.random.random() < self.epsilon
            ## 将之前的 choose_action 的判断放到这里
            
        if self.learning:
        ## 如果是学习状态
            if is_random_exploration():
                # TODO 6. Return random choose aciton
                action = np.random.choice(self.valid_actions)
                return action
            else: 
                # TODO 7. Return action with highest q value
                action = max(self.Qtable[self.state], key=self.Qtable[self.state].get)
                return action
        elif self.testing:
            # TODO 7. choose action with highest q value
            action = max(self.Qtable[self.state], key=self.Qtable[self.state].get)
            return action
        else:
            # TODO 6. Return random choose aciton
            action = random.choice(self.valid_actions)
            return action
        ## 此处感觉可以简化为 else 直接使用最大值（测试），去掉 elseif

    def update_Qtable(self, r, action, next_state):
        """
        Update the qtable according to the given rule.
        """
        if self.learning:
            # TODO 8. When learning, update the q table according
            # to the given rules
            current = self.Qtable[self.state][action]
            
            # q_target = r + self.gamma * float(max(self.Qtable[next_state].values()))
            # target = r + self.gamma * (max(self.Qtable[next_state].values()))
            target = r + self.gamma * (max(self.Qtable[next_state].values()))
            ## 更新后的目标值是在这一步获得的 r 上增加后续的值
            ## gamma 是对未来的惩罚，r 是输入的这步的 reward
            
            self.Qtable[self.state][action] = (1-self.alpha) * self.Qtable[self.state][action] + self.alpha * (target - current)
            ## 根据学习率 alpha，更新Q值

    def update(self):
        """
        Describle the procedure what to do when update the robot.
        Called every time in every epoch in training or testing.
        Return current action and reward.
        """
        self.state = self.sense_state() 
        # Get the current state
        ## 获得机器人的位置
        
        self.create_Qtable_line(self.state) 
        # For the state, create q table line
        ## 获得现在的Qtable

        action = self.choose_action() 
        # choose action for this state
        ## 选择一个方向
        
        reward = self.maze.move_robot(action) 
        # move robot for given action
        ## 移动机器人并将这步的奖励值赋给reward

        next_state = self.sense_state() 
        # get next state
        ## 获得新的位置（因为上面已经move过了）
        
        self.create_Qtable_line(next_state) 
        # create q table line for next state
        ## 初始化下一步的Qtable

        if self.learning and not self.testing:
            ## 如果是学习状态
            self.update_Qtable(reward, action, next_state) 
            # update q table
            ## 更新Qtable
            self.update_parameter() 
            # update parameters
            ## 更新参数

        return action, reward
        # 返回这步的方向和得到的奖励