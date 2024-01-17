import maya.cmds as cmds

def create_tornado_emitter():
    # Create a sphere
    sphere = cmds.polySphere(name='TornadoSphere')[0]

    # Create a particle emitter
    emitter = cmds.emitter(sphere, type='omni', rate=100, name='TornadoEmitter')[0]
    particle = cmds.particle(name='TornadoParticles')[0]

    # Connect emitter to particle
    cmds.connectDynamic(particle, em=emitter)

    # Create fields for tornado effect
    turbulence = cmds.turbulence(name='TurbulenceField', m=5, att=0.1, frequency=2)
    vortex = cmds.vortex(name='VortexField', m=5, axis=(0, 1, 0))

    # Add fields to particles
    cmds.connectDynamic(particle, f=turbulence[0])
    cmds.connectDynamic(particle, f=vortex[0])

    # Adjust vortex to create a swirling motion
    cmds.setAttr(vortex[0] + '.magnitude', 10)
    cmds.setAttr(vortex[0] + '.axisY', 1)

create_tornado_emitter()
