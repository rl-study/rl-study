from ten_armed_testbed import Bandit;

bandit = Bandit(k_arm=5, epsilon=0.1)
steps = 500
show_each_step = False

bandit.reset()
print("Best action : " + str(bandit.best_action))
last_ten_actions = []

def print_out(step, last_ten_actions, reward):
    print("Step : " + str(step) + ", action : " + str(last_ten_actions[0]) + ", reward : " + "{:.2f}".format(reward))
    print("\ttrue values : " + '%s' % ', '.join(map("{:.2f}".format, bandit.q_true)))
    print("\testimations : " + '%s' % ', '.join(map("{:.2f}".format, bandit.q_estimation)))
    print("\taction_count : " + '%s' % ', '.join(map("{:.0f}".format, bandit.action_count)))
    print("\tlast ten actions : " + '%s' % ', '.join(map(str, last_ten_actions)))
    
def one_step(step, show_each_step=False):
    action = bandit.act()
    last_ten_actions.insert(0,action)
    if len(last_ten_actions) > 10:
        del last_ten_actions[-1]
    reward = bandit.step(action)
    if step == steps:
        print_out(step, last_ten_actions, reward)
    else:
        if show_each_step == True:
            print_out(step, last_ten_actions, reward)

for i in range(1,steps+1):
    one_step(i,show_each_step)
