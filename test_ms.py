#!/usr/bin/env python
# encoding: utf-8
'''
test_ms.py - test for Providence Salumu from 
Morgan Stanley | Institutional Securities Tech   

It is raw and not well tested version.
But I hope the idea is understandable 

@author:     Serguei Koubli
'''

import sys
from itertools import permutations

def fill_track(tracks, track, slot_num, grph, sport):
    if track not in tracks:
        tracks[track] = {}
        
    if sport not in grph:
        return
    
    sports = grph.pop(sport)
    for s in sports:
        slot_num += 1
        tracks[track][slot_num] = s
        fill_track(tracks, track, slot_num, grph, s)
        
def create_incompatibility_graph(athletes, max_slots):
    # genereting set of the sports from list of the athlets
    sports = set()
    for sm, sps in athletes.items():
        for sp in sps:
            sports.add(sp) 
            
    # creating graph of intcompatible sports base on athlets list
    # and their abilities
    grph = {}
    max_slots = '';
    max_incomp_list_key = None
    for s in sports:
        grph[s] = list(sports)
        for sm, sps in athletes.items():
            if s in sps:
                for sp in sps:
                    if sp in grph[s]:
                        grph[s].remove(sp)
        max_incomp_list_key = s if not max_incomp_list_key or len(grph[s]) > len(grph[max_incomp_list_key]) else max_incomp_list_key
        # max_incomp_list_key related code it just for optimisation
        if len(grph[max_incomp_list_key]) > max_slots:
            print "not enough slots"
            return {}, max_incomp_list_key

    return grph, max_incomp_list_key
       
def get_billet_graph(athletes, max_slots):
    grph, max_incomp_list = create_incompatibility_graph(athletes, max_slots)
    if not len(grph):
        return {}
    
    tracks = {}
    def_track = 1
    def_slot = 1
    fill_track(tracks, def_track, def_slot - 1, grph, max_incomp_list)
    for s in grph.keys():
        def_track += 1
        if def_track not in grph:
            tracks[def_track] = {}
            
        tracks[def_track][def_slot] = s  
        
    return tracks

def get_default_schedule(athletes, max_tracks, max_slots):
    tracks = get_billet_graph(athletes, max_slots)
    if not len(tracks):
        return [];
    
    if len(tracks) > max_tracks:
        # TODO: just skeep it for now
        print "not enough tracks."
        "\nTODO: move if posiile to other slots or add more slots"
    
    # filling extra slots for used tracks
    for track in tracks:
        for slot in xrange(len(tracks[track]) + 1, max_slots + 1):
            tracks[track][slot] = 'x'
        
    # adding extra tracks if need
    for track in xrange(len(tracks) + 1, max_tracks + 1):
        tracks[track] = {x:'x' for x in xrange(1, max_slots + 1)}
        
    return tracks
    
def print_schedule(sched, tracks, slots):
    #print tracks, slots
    #TODO: need to improve printout of table
    track_n = 0
    for track in tracks:
        track_n += 1
        print track_n, " |\t",
        for slot in slots:
            print sched[track][slot], "\t|\t",
        print ''
    print ""

def print_all_schedules(athletes, max_tracks, max_slots):
    def_schedule = get_default_schedule(athletes, max_tracks, max_slots)    
    if not len(def_schedule):
        print "can't generate anything(("
        return
    
    for x in permutations(def_schedule.keys(), len(def_schedule)):
        for y in permutations(def_schedule[x[0]].keys(), len(def_schedule[x[0]])):
            print_schedule(def_schedule, x, y)


def main(argv=None):
    #TODO: need to parsing argument. Hardcoded for now
    athletes = {'m1':['s1', 's2', 's3'], 'm2':['s1', 's2'], 'm3':['s2', 's3', 's4'], 'm4':['s4']}
    max_tracks = 5
    max_slots = 3
        
    print_all_schedules(athletes, max_tracks, max_slots)
        
if __name__ == "__main__":
    sys.exit(main())

