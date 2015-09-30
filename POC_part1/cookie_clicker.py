"""
Cookie Clicker Simulator
"""

import simpleplot
import math

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._total_cookies = 0.0
        self._current_cookies = 0.0
        self._time = 0.0
        self._cps = 1.0
        self._history = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        return "\nTotal cookies owned: " + str(self._total_cookies) + "\nCurrent cookies: " + str(self._current_cookies) + "\nCurrent time: " + str(self._time) + "\nCurrent cps: " + str(self._cps)
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._current_cookies
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return [item for item in self._history]

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        result = math.ceil((cookies - self._current_cookies) / self._cps)
        return max(result, 0.0)
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if (time > 0):
            self._time += time
            self._current_cookies += self._cps * time
            self._total_cookies += self._cps * time
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if (self._current_cookies >= cost):
            self._history.append((self._time, item_name, cost, self._total_cookies))
            self._current_cookies -= cost
            self._cps += additional_cps
            
    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """

    # Replace with your code
    state = ClickerState()
    build = build_info.clone()
    while (state.get_time() <= duration):
        item = strategy(state.get_cookies(), state.get_cps(), state.get_history(), duration - state.get_time(), build)
        if (item == None):
            break
        cost = build.get_cost(item)
        cps = build.get_cps(item)
        build.update_item(item)
        time = state.time_until(cost)
        if (time + state.get_time() > duration):
            break
        state.wait(time)
        state.buy_item(item, cost, cps)
    state.wait(duration - state.get_time())
    return state

def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    item_list = build_info.build_items()
    max_cost = time_left * cps + cookies
    result = item_list[0]
    min_cost = build_info.get_cost(result)
    for item in item_list:
        if (build_info.get_cost(item) < min_cost):
            result = item
    if (build_info.get_cost(result) <= max_cost):
        return result
    else:
        return None

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    item_list = build_info.build_items()
    max_cost = time_left * cps + cookies
    result = item_list[0]
    result_cost = build_info.get_cost(result)
    for item in item_list:
        cost = build_info.get_cost(item)
        if (cost > result_cost and cost <= max_cost):
            result = item
    if (build_info.get_cost(result) <= max_cost):
        return result
    else:
        return None

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    item_list = build_info.build_items()
    eff_dict = {}
    for item in item_list:
        eff_dict[build_info.get_cps(item) / build_info.get_cost(item)] = item
    eff_list = sorted(eff_dict.keys())
    idx = len(eff_list) - 1
    while (idx >= 0):
        item = eff_dict[eff_list[idx]]
        if (build_info.get_cost(item) <= cps * time_left + cookies):
            return item
        idx -= 1
    return None
        
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    #run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)
    #run_strategy("Cheap", SIM_TIME, strategy_cheap)
    #run_strategy("Expensive", SIM_TIME, strategy_expensive)
    #run_strategy("Best", SIM_TIME, strategy_best)

    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)
    
run()

