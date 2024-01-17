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

    # Create an Arnold Standard Volume shader
    shader = cmds.shadingNode('aiStandardVolume', asShader=True, name='ParticleShader')
    shading_group = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=shader + 'SG')
    cmds.connectAttr(shader + '.outColor', shading_group + '.volumeShader', force=True)

    # Assign the shader to the particle shape node
    particle_shape = cmds.listRelatives(particle, shapes=True)[0]
    cmds.select(particle_shape)
    cmds.hyperShade(assign=shader)

create_tornado_emitter()