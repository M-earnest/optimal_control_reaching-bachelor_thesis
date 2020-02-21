"""
This module was generated by Vizconnect.
Version: 1.05
Generated on: 2019-06-18 09:00:48.783000
"""

import viz
import vizconnect

#################################
# Parent configuration, if any
#################################

def getParentConfiguration():
	#VC: set the parent configuration
	_parent = ''
	
	#VC: return the parent configuration
	return _parent


#################################
# Pre viz.go() Code
#################################

def preVizGo():
	return True


#################################
# Pre-initialization Code
#################################

def preInit():
	"""Add any code here which should be called after viz.go but before any initializations happen.
	Returned values can be obtained by calling getPreInitResult for this file's vizconnect.Configuration instance."""
	return None


#################################
# Group Code
#################################

def initGroups(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawGroup = vizconnect.getRawGroupDict()
	
	#VC: return values can be modified here
	return None


#################################
# Display Code
#################################

def initDisplays(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawDisplay = vizconnect.getRawDisplayDict()

	#VC: return values can be modified here
	return None


#################################
# Tracker Code
#################################

def initTrackers(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawTracker = vizconnect.getRawTrackerDict()

	#VC: initialize a new tracker
	_name = 'marker2'
	if vizconnect.isPendingInit('tracker', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			hostname = '127.0.0.1:2'
			sensorIndex = 14
			
			#VC: create the raw object
			try:
				phasespace = viz.add('phasespace.dle',0,hostname)
			except:
				viz.logWarn("** WARNING: can't connect to PhaseSpace at {0}.".format(hostname))
			
			validTracker = False
			if phasespace.id != -1:
				try:
					sensor = phasespace.addMarker(sensorIndex)
					validTracker = True
				except:
					validTracker = False
			
			if not validTracker:
				viz.logWarn("** WARNING: can't connect to Northern Digital Optotrack with index {0}. It's likely that not enough sensors are connected.".format(sensorIndex))
				sensor = viz.addGroup()
				sensor.invalidTracker = True
			rawTracker[_name] = sensor
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTracker(rawTracker[_name], _name, make='PhaseSpace', model='Marker')

	#VC: initialize a new tracker
	_name = 'look_at'
	if vizconnect.isPendingInit('tracker', _name, initFlag, initList):
		#VC: request that any dependencies be created
		if initFlag&vizconnect.INIT_INDEPENDENT:
			initTrackers(vizconnect.INIT_INDEPENDENT, ['marker2'])
			initTrackers(vizconnect.INIT_INDEPENDENT, ['marker3'])
	
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			eye = vizconnect.getTracker('marker2').getNode3d()
			target = vizconnect.getTracker('marker3').getNode3d()
			
			#VC: create the raw object
			from vizconnect.util import virtual_trackers
			if eye and target:
				raw = virtual_trackers.LookAt(eye=eye, target=target)
			else:
				viz.logError('Error **: unable to create merged tracker, providing empty tracker object.')
				raw = viz.addGroup()
				raw.invalidTracker = True
			rawTracker[_name] = raw
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTracker(rawTracker[_name], _name, make='Virtual', model='Look At')
	
		#VC: init the offsets
		if initFlag&vizconnect.INIT_OFFSETS:
			_link = vizconnect.getTracker(_name).getLink()
			#VC: clear link offsets
			_link.reset(viz.RESET_OPERATORS)
			
			#VC: apply offsets
			_link.postEuler([0, 0, 2])

	#VC: initialize a new tracker
	_name = 'marker3'
	if vizconnect.isPendingInit('tracker', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			hostname = '127.0.0.1:2'
			sensorIndex = 15
			
			#VC: create the raw object
			try:
				phasespace = viz.add('phasespace.dle',0,hostname)
			except:
				viz.logWarn("** WARNING: can't connect to PhaseSpace at {0}.".format(hostname))
			
			validTracker = False
			if phasespace.id != -1:
				try:
					sensor = phasespace.addMarker(sensorIndex)
					validTracker = True
				except:
					validTracker = False
			
			if not validTracker:
				viz.logWarn("** WARNING: can't connect to Northern Digital Optotrack with index {0}. It's likely that not enough sensors are connected.".format(sensorIndex))
				sensor = viz.addGroup()
				sensor.invalidTracker = True
			rawTracker[_name] = sensor
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTracker(rawTracker[_name], _name, make='PhaseSpace', model='Marker')

	#VC: initialize a new tracker
	_name = 'head_0'
	if vizconnect.isPendingInit('tracker', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			hostname = '127.0.0.1:2'
			sensorIndex = 3
			
			#VC: create the raw object
			try:
				phasespace = viz.add('phasespace.dle',0,hostname)
			except:
				viz.logWarn("** WARNING: can't connect to PhaseSpace at {0}.".format(hostname))
			
			validTracker = False
			if phasespace.id != -1:
				try:
					sensor = phasespace.addMarker(sensorIndex)
					validTracker = True
				except:
					validTracker = False
			
			if not validTracker:
				viz.logWarn("** WARNING: can't connect to Northern Digital Optotrack with index {0}. It's likely that not enough sensors are connected.".format(sensorIndex))
				sensor = viz.addGroup()
				sensor.invalidTracker = True
			rawTracker[_name] = sensor
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTracker(rawTracker[_name], _name, make='PhaseSpace', model='Marker')

	#VC: initialize a new tracker
	_name = 'marker'
	if vizconnect.isPendingInit('tracker', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			hostname = '127.0.0.1:2'
			sensorIndex = 0
			
			#VC: create the raw object
			try:
				phasespace = viz.add('phasespace.dle',0,hostname)
			except:
				viz.logWarn("** WARNING: can't connect to PhaseSpace at {0}.".format(hostname))
			
			validTracker = False
			if phasespace.id != -1:
				try:
					sensor = phasespace.addMarker(sensorIndex)
					validTracker = True
				except:
					validTracker = False
			
			if not validTracker:
				viz.logWarn("** WARNING: can't connect to Northern Digital Optotrack with index {0}. It's likely that not enough sensors are connected.".format(sensorIndex))
				sensor = viz.addGroup()
				sensor.invalidTracker = True
			rawTracker[_name] = sensor
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTracker(rawTracker[_name], _name, make='PhaseSpace', model='Marker')

	#VC: initialize a new tracker
	_name = 'look_at2'
	if vizconnect.isPendingInit('tracker', _name, initFlag, initList):
		#VC: request that any dependencies be created
		if initFlag&vizconnect.INIT_INDEPENDENT:
			initTrackers(vizconnect.INIT_INDEPENDENT, ['head_0'])
			initTrackers(vizconnect.INIT_INDEPENDENT, ['marker'])
	
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			eye = vizconnect.getTracker('head_0').getNode3d()
			target = vizconnect.getTracker('marker').getNode3d()
			
			#VC: create the raw object
			from vizconnect.util import virtual_trackers
			if eye and target:
				raw = virtual_trackers.LookAt(eye=eye, target=target)
			else:
				viz.logError('Error **: unable to create merged tracker, providing empty tracker object.')
				raw = viz.addGroup()
				raw.invalidTracker = True
			rawTracker[_name] = raw
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTracker(rawTracker[_name], _name, make='Virtual', model='Look At')

	#VC: initialize a new tracker
	_name = 'marker4'
	if vizconnect.isPendingInit('tracker', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			hostname = '127.0.0.1:2'
			sensorIndex = 21
			
			#VC: create the raw object
			try:
				phasespace = viz.add('phasespace.dle',0,hostname)
			except:
				viz.logWarn("** WARNING: can't connect to PhaseSpace at {0}.".format(hostname))
			
			validTracker = False
			if phasespace.id != -1:
				try:
					sensor = phasespace.addMarker(sensorIndex)
					validTracker = True
				except:
					validTracker = False
			
			if not validTracker:
				viz.logWarn("** WARNING: can't connect to Northern Digital Optotrack with index {0}. It's likely that not enough sensors are connected.".format(sensorIndex))
				sensor = viz.addGroup()
				sensor.invalidTracker = True
			rawTracker[_name] = sensor
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTracker(rawTracker[_name], _name, make='PhaseSpace', model='Marker')

	#VC: initialize a new tracker
	_name = 'marker5'
	if vizconnect.isPendingInit('tracker', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			hostname = '127.0.0.1:2'
			sensorIndex = 22
			
			#VC: create the raw object
			try:
				phasespace = viz.add('phasespace.dle',0,hostname)
			except:
				viz.logWarn("** WARNING: can't connect to PhaseSpace at {0}.".format(hostname))
			
			validTracker = False
			if phasespace.id != -1:
				try:
					sensor = phasespace.addMarker(sensorIndex)
					validTracker = True
				except:
					validTracker = False
			
			if not validTracker:
				viz.logWarn("** WARNING: can't connect to Northern Digital Optotrack with index {0}. It's likely that not enough sensors are connected.".format(sensorIndex))
				sensor = viz.addGroup()
				sensor.invalidTracker = True
			rawTracker[_name] = sensor
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTracker(rawTracker[_name], _name, make='PhaseSpace', model='Marker')

	#VC: initialize a new tracker
	_name = 'look_at3'
	if vizconnect.isPendingInit('tracker', _name, initFlag, initList):
		#VC: request that any dependencies be created
		if initFlag&vizconnect.INIT_INDEPENDENT:
			initTrackers(vizconnect.INIT_INDEPENDENT, ['marker4'])
			initTrackers(vizconnect.INIT_INDEPENDENT, ['marker5'])
	
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			eye = vizconnect.getTracker('marker4').getNode3d()
			target = vizconnect.getTracker('marker5').getNode3d()
			
			#VC: create the raw object
			from vizconnect.util import virtual_trackers
			if eye and target:
				raw = virtual_trackers.LookAt(eye=eye, target=target)
			else:
				viz.logError('Error **: unable to create merged tracker, providing empty tracker object.')
				raw = viz.addGroup()
				raw.invalidTracker = True
			rawTracker[_name] = raw
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTracker(rawTracker[_name], _name, make='Virtual', model='Look At')

	#VC: initialize a new tracker
	_name = 'marker6'
	if vizconnect.isPendingInit('tracker', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			hostname = '127.0.0.1:2'
			sensorIndex = 12
			
			#VC: create the raw object
			try:
				phasespace = viz.add('phasespace.dle',0,hostname)
			except:
				viz.logWarn("** WARNING: can't connect to PhaseSpace at {0}.".format(hostname))
			
			validTracker = False
			if phasespace.id != -1:
				try:
					sensor = phasespace.addMarker(sensorIndex)
					validTracker = True
				except:
					validTracker = False
			
			if not validTracker:
				viz.logWarn("** WARNING: can't connect to Northern Digital Optotrack with index {0}. It's likely that not enough sensors are connected.".format(sensorIndex))
				sensor = viz.addGroup()
				sensor.invalidTracker = True
			rawTracker[_name] = sensor
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTracker(rawTracker[_name], _name, make='PhaseSpace', model='Marker')

	#VC: return values can be modified here
	return None


#################################
# Input Code
#################################

def initInputs(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawInput = vizconnect.getRawInputDict()
	
	#VC: return values can be modified here
	return None


#################################
# Event Code
#################################

def initEvents(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawEvent = vizconnect.getRawEventDict()
	
	#VC: return values can be modified here
	return None


#################################
# Transport Code
#################################

def initTransports(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawTransport = vizconnect.getRawTransportDict()
	
	#VC: return values can be modified here
	return None


#################################
# Tool Code
#################################

def initTools(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawTool = vizconnect.getRawToolDict()
	
	#VC: return values can be modified here
	return None


#################################
# Avatar Code
#################################

def initAvatars(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawAvatar = vizconnect.getRawAvatarDict()

	#VC: initialize a new avatar
	_name = 'male'
	if vizconnect.isPendingInit('avatar', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: create the raw object
			avatar = viz.add('vcc_male.cfg')
			avatar._bodyPartDict = {}
			avatar._handModelDict = {}
			rawAvatar[_name] = avatar
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addAvatar(rawAvatar[_name], _name, make='Complete Characters', model='Male')
	
		#VC: init the animator
		if initFlag&vizconnect.INIT_ANIMATOR:
			# need to get the raw tracker dict for animating the avatars
			from vizconnect.util.avatar import animator
			from vizconnect.util.avatar import skeleton
			
			# get the skeleton from the avatar
			_skeleton = skeleton.CompleteCharacters(rawAvatar[_name])
			
			#VC: set which trackers animate which body part
			# format is: bone: (tracker, parent, degrees of freedom used)
			_trackerAssignmentDict = {
				vizconnect.AVATAR_HEAD:(vizconnect.getTracker('look_at2').getNode3d(), None, vizconnect.DOF_6DOF),
				vizconnect.AVATAR_L_FOREARM:(vizconnect.getTracker('marker6').getNode3d(), None, vizconnect.DOF_6DOF),
				vizconnect.AVATAR_L_HAND:(vizconnect.getTracker('look_at').getNode3d(), None, vizconnect.DOF_6DOF),
				vizconnect.AVATAR_R_HAND:(vizconnect.getTracker('look_at3').getNode3d(), None, vizconnect.DOF_6DOF),
			}
			
			#VC: create the raw object
			_rawAnimator = animator.InverseKinematics(rawAvatar[_name], _skeleton, _trackerAssignmentDict)
			
			#VC: set animator in wrapper (DO NOT EDIT)
			vizconnect.getAvatar(_name).setAnimator(_rawAnimator, make='WorldViz', model='Inverse Kinematics')

	#VC: return values can be modified here
	return None


#################################
# Application Settings
#################################

def initSettings():
	#VC: apply general application settings
	viz.mouse.setTrap(False)
	viz.mouse.setVisible(viz.MOUSE_AUTO_HIDE)
	vizconnect.setMouseTrapToggleKey('')
	
	#VC: return values can be modified here
	return None


#################################
# Post-initialization Code
#################################

def postInit():
	"""Add any code here which should be called after all of the initialization of this configuration is complete.
	Returned values can be obtained by calling getPostInitResult for this file's vizconnect.Configuration instance."""
	return None


#################################
# Stand alone configuration
#################################

def initInterface():
	#VC: start the interface
	vizconnect.interface.go(__file__,
							live=True,
							openBrowserWindow=True,
							startingInterface=vizconnect.interface.INTERFACE_STARTUP)

	#VC: return values can be modified here
	return None


###############################################

if __name__ == "__main__":
	initInterface()
	viz.add('piazza.osgb')
	viz.add('piazza_animations.osgb')

