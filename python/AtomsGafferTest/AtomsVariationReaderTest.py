##########################################################################
#
#  Copyright (c) 2018, Toolchefs Ltd. All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#      * Redistributions of source code must retain the above
#        copyright notice, this list of conditions and the following
#        disclaimer.
#
#      * Redistributions in binary form must reproduce the above
#        copyright notice, this list of conditions and the following
#        disclaimer in the documentation and/or other materials provided with
#        the distribution.
#
#      * Neither the name of John Haddon nor the names of
#        any other contributors to this software may be used to endorse or
#        promote products derived from this software without specific prior
#        written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
#  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
#  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
#  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
##########################################################################

import unittest
import imath

import IECore
import IECoreScene

import GafferTest
import GafferSceneTest

import AtomsGaffer

class AtomsVariationReaderTest( GafferSceneTest.SceneTestCase ) :

	def testConstruct( self ) :

		a = AtomsGaffer.AtomsVariationReader()
		self.assertEqual( a.getName(), "AtomsVariationReader" )

	def testChildNames( self ) :

		node = AtomsGaffer.AtomsVariationReader()
		node["atomsVariationFile"].setValue( "${ATOMS_GAFFER_ROOT}/examples/assets/atomsRobot/atomsRobot.json" )

		names = node["out"].childNames( "/" )
		self.assertEqual( len(names), 2 )
		self.assertTrue( "atomsRobot" in names )
		self.assertTrue( "atoms2Robot" in names )

		names = node["out"].childNames( "/atoms2Robot" )
		self.assertEqual( len(names), 4 )
		self.assertTrue( "RedRobot" in names )
		self.assertTrue( "RedRobot:A" in names )
		self.assertTrue( "PurpleRobot" in names )
		self.assertTrue( "YellowRobot" in names )

		names = node["out"].childNames( "/atoms2Robot/RedRobot" )
		self.assertTrue( "Body" in names )

		names = node["out"].childNames( "/atoms2Robot/RedRobot/Body" )
		self.assertEqual( len(names), 1 )
		self.assertTrue( "RobotBody" in names)

		names = node["out"].childNames( "/atoms2Robot/RedRobot:A" )
		self.assertTrue( "Body" in names )

		names = node["out"].childNames( "/atoms2Robot/RedRobot:A/Body" )
		self.assertEqual( len(names), 1 )
		self.assertTrue( "RobotBody" in names)

		names = node["out"].childNames( "/atoms2Robot/PurpleRobot" )
		self.assertTrue( "Body" in names )

		names = node["out"].childNames( "/atoms2Robot/PurpleRobot/Body" )
		self.assertEqual( len(names), 1 )
		self.assertTrue( "RobotBody" in names)

		names = node["out"].childNames( "/atoms2Robot/YellowRobot" )
		self.assertTrue( "Body" in names )

		names = node["out"].childNames( "/atoms2Robot/YellowRobot/Body" )
		self.assertEqual( len(names), 1 )
		self.assertTrue( "RobotBody" in names)

		names = node["out"].childNames( "/atomsRobot" )
		self.assertEqual( len(names), 6 )
		self.assertTrue( "Robot1" in names )
		self.assertTrue( "Robot1:A" in names )
		self.assertTrue( "Robot1:B" in names )
		self.assertTrue( "Robot2" in names )
		self.assertTrue( "Robot2:A" in names )
		self.assertTrue( "Robot2:B" in names )

		names = node["out"].childNames( "/atomsRobot/Robot1" )
		self.assertTrue( "RobotSkin1" in names)

		names = node["out"].childNames( "/atomsRobot/Robot1/RobotSkin1" )
		self.assertTrue( "arms" in names)
		self.assertTrue( "body" in names)
		self.assertTrue( "legs" in names)
		self.assertTrue( "head" in names)
		self.assertTrue( "flag_group" in names)

		names = node["out"].childNames( "/atomsRobot/Robot1/RobotSkin1/head" )
		self.assertTrue( "robot1_head" in names)

		names = node["out"].childNames( "/atomsRobot/Robot1/RobotSkin1/body" )
		self.assertTrue( "robot1_body" in names)

		names = node["out"].childNames( "/atomsRobot/Robot1:A/RobotSkin1/head" )
		self.assertTrue( "robot1_head" in names)

		names = node["out"].childNames( "/atomsRobot/Robot1:A/RobotSkin1/body" )
		self.assertTrue( "robot1_body" in names)

		names = node["out"].childNames( "/atomsRobot/Robot1:B/RobotSkin1/body" )
		self.assertTrue( "robot1_body" in names)

		names = node["out"].childNames( "/atomsRobot/Robot2" )
		self.assertTrue( "robot2_head" in names)
		self.assertTrue( "robot2_body" in names)
		self.assertTrue( "robot2_arms" in names)
		self.assertTrue( "robot2_legs" in names)

		names = node["out"].childNames( "/atomsRobot/Robot2:A" )
		self.assertTrue( "robot2_head" in names)
		self.assertTrue( "robot2_body" in names)

		names = node["out"].childNames( "/atomsRobot/Robot2:B" )
		self.assertTrue( "robot2_body" in names)

	def testCompute( self ) :

		node = AtomsGaffer.AtomsVariationReader()
		node["atomsVariationFile"].setValue( "${ATOMS_GAFFER_ROOT}/examples/assets/atomsRobot/atomsRobot.json" )

		obj = node["out"].object( "/atomsRobot/Robot1/RobotSkin1/head/robot1_head" )
		self.assertEqual( obj.typeName(), IECoreScene.MeshPrimitive.staticTypeName() )
		self.assertEqual( len(obj["P"].data), 920 )
		self.assertEqual( len(obj["N"].data), 3480 )
		self.assertEqual( len(obj["uv"].data), 1533 )
		self.assertEqual( len(obj["blendShape_0_P"].data), 920 )
		self.assertEqual( len(obj["blendShape_0_N"].data), 3480 )
		self.assertEqual( len(obj["blendShape_1_P"].data), 920 )
		self.assertEqual( len(obj["blendShape_1_N"].data), 3480 )
		self.assertEqual( obj["blendShapeCount"].data.value, 2 )

		obj = node["out"].object( "/atomsRobot/Robot1/RobotSkin1/body/robot1_body" )
		self.assertEqual( obj.typeName(), IECoreScene.MeshPrimitive.staticTypeName() )
		self.assertEqual( len(obj["P"].data), 635 )
		self.assertEqual( len(obj["N"].data), 2356 )
		self.assertEqual( len(obj["uv"].data), 1222 )

		obj = node["out"].object( "/atomsRobot/Robot1/RobotSkin1/arms/robot1_arms" )
		self.assertEqual( obj.typeName(), IECoreScene.MeshPrimitive.staticTypeName() )
		self.assertEqual( len(obj["P"].data), 960 )
		self.assertEqual( len(obj["N"].data), 3424 )
		self.assertEqual( len(obj["uv"].data), 1832 )
		self.assertEqual( len(obj["primFaceAttr"].data), 828 )
		self.assertEqual( len(obj["primObjAttr"].data), 1 )
		self.assertEqual( len(obj["primVertsAttr"].data), 960 )

		obj = node["out"].object( "/atomsRobot/Robot1/RobotSkin1/legs/robot1_legs" )
		self.assertEqual( obj.typeName(), IECoreScene.MeshPrimitive.staticTypeName() )
		self.assertEqual( len(obj["P"].data), 904 )
		self.assertEqual( len(obj["N"].data), 3312 )
		self.assertEqual( len(obj["uv"].data), 1516 )

		obj = node["out"].object( "/atomsRobot/Robot1:A/RobotSkin1/head/robot1_head" )
		self.assertEqual( obj.typeName(), IECoreScene.MeshPrimitive.staticTypeName() )
		self.assertEqual( len(obj["P"].data), 920 )
		self.assertEqual( len(obj["N"].data), 3480 )
		self.assertEqual( len(obj["uv"].data), 1533 )
		self.assertEqual( len(obj["blendShape_0_P"].data), 920 )
		self.assertEqual( len(obj["blendShape_0_N"].data), 3480 )
		self.assertEqual( len(obj["blendShape_1_P"].data), 920 )
		self.assertEqual( len(obj["blendShape_1_N"].data), 3480 )
		self.assertEqual( obj["blendShapeCount"].data.value, 2 )

		obj = node["out"].object( "/atomsRobot/Robot1:A/RobotSkin1/flag_group/pPlane1" )
		self.assertEqual( obj.typeName(), IECoreScene.MeshPrimitive.staticTypeName() )
		self.assertEqual( len(obj["P"].data), 121 )
		self.assertEqual( len(obj["N"].data), 400 )
		self.assertEqual( len(obj["uv"].data), 121 )

		obj = node["out"].object( "/atomsRobot/Robot1:A/RobotSkin1/flag_group/pole" )
		self.assertEqual( obj.typeName(), IECoreScene.MeshPrimitive.staticTypeName() )
		self.assertEqual( len(obj["P"].data), 1022 )
		self.assertEqual( len(obj["N"].data), 4120 )
		self.assertEqual( len(obj["uv"].data), 1113 )

		obj = node["out"].object( "/atomsRobot/Robot1:A/RobotSkin1/body/robot1_body" )
		self.assertEqual( obj.typeName(), IECoreScene.MeshPrimitive.staticTypeName() )
		self.assertEqual( len(obj["P"].data), 635 )
		self.assertEqual( len(obj["N"].data), 2356 )
		self.assertEqual( len(obj["uv"].data), 1222 )

		obj = node["out"].object( "/atomsRobot/Robot1:B/RobotSkin1/body/robot1_body" )
		self.assertEqual( obj.typeName(), IECoreScene.MeshPrimitive.staticTypeName() )
		self.assertEqual( len(obj["P"].data), 635 )
		self.assertEqual( len(obj["N"].data), 2356 )
		self.assertEqual( len(obj["uv"].data), 1222 )

		obj = node["out"].object( "/atomsRobot/Robot2/robot2_head" )
		self.assertEqual( obj.typeName(), IECoreScene.MeshPrimitive.staticTypeName() )
		self.assertEqual( len(obj["P"].data), 5874 )
		self.assertEqual( len(obj["N"].data), 5874 )
		self.assertEqual( len(obj["uv"].data), 5874 )

		obj = node["out"].object( "/atomsRobot/Robot2/robot2_body" )
		self.assertEqual( obj.typeName(), IECoreScene.MeshPrimitive.staticTypeName() )
		self.assertEqual( len(obj["P"].data), 16944 )
		self.assertEqual( len(obj["N"].data), 16944 )
		self.assertEqual( len(obj["uv"].data), 16944 )

		obj = node["out"].object( "/atomsRobot/Robot2/robot2_arms" )
		self.assertEqual( obj.typeName(), IECoreScene.MeshPrimitive.staticTypeName() )
		self.assertEqual( len(obj["P"].data), 6288 )
		self.assertEqual( len(obj["N"].data), 6288 )
		self.assertEqual( len(obj["uv"].data), 6288 )

		obj = node["out"].object( "/atomsRobot/Robot2/robot2_legs" )
		self.assertEqual( obj.typeName(), IECoreScene.MeshPrimitive.staticTypeName() )
		self.assertEqual( len(obj["P"].data), 7200 )
		self.assertEqual( len(obj["N"].data), 7200 )
		self.assertEqual( len(obj["uv"].data), 7200 )

		obj = node["out"].object( "/atomsRobot/Robot2:A/robot2_head" )
		self.assertEqual( obj.typeName(), IECoreScene.MeshPrimitive.staticTypeName() )
		self.assertEqual( len(obj["P"].data), 5874 )
		self.assertEqual( len(obj["N"].data), 5874 )
		self.assertEqual( len(obj["uv"].data), 5874 )

		obj = node["out"].object( "/atomsRobot/Robot2:A/robot2_body" )
		self.assertEqual( obj.typeName(), IECoreScene.MeshPrimitive.staticTypeName() )
		self.assertEqual( len(obj["P"].data), 16944 )
		self.assertEqual( len(obj["N"].data), 16944 )
		self.assertEqual( len(obj["uv"].data), 16944 )

		obj = node["out"].object( "/atomsRobot/Robot2:B/robot2_body" )
		self.assertEqual( obj.typeName(), IECoreScene.MeshPrimitive.staticTypeName() )
		self.assertEqual( len(obj["P"].data), 16944 )
		self.assertEqual( len(obj["N"].data), 16944 )
		self.assertEqual( len(obj["uv"].data), 16944 )

		obj = node["out"].object( "/atoms2Robot/YellowRobot/Body/RobotBody" )
		self.assertEqual( obj.typeName(), IECoreScene.MeshPrimitive.staticTypeName() )
		self.assertEqual( len(obj["P"].data), 28149 )
		self.assertEqual( len(obj["N"].data), 111930 )
		self.assertEqual( len(obj["uv"].data), 31402 )

		obj = node["out"].object( "/atoms2Robot/RedRobot/Body/RobotBody" )
		self.assertEqual( obj.typeName(), IECoreScene.MeshPrimitive.staticTypeName() )
		self.assertEqual( len(obj["P"].data), 28149 )
		self.assertEqual( len(obj["N"].data), 111930 )
		self.assertEqual( len(obj["uv"].data), 31402 )

		obj = node["out"].object( "/atoms2Robot/RedRobot:A/Body/RobotBody" )
		self.assertEqual( obj.typeName(), IECoreScene.MeshPrimitive.staticTypeName() )
		self.assertEqual( len(obj["P"].data), 28149 )
		self.assertEqual( len(obj["N"].data), 111930 )
		self.assertEqual( len(obj["uv"].data), 31402 )

		obj = node["out"].object( "/atoms2Robot/PurpleRobot/Body/RobotBody" )
		self.assertEqual( obj.typeName(), IECoreScene.MeshPrimitive.staticTypeName() )
		self.assertEqual( len(obj["P"].data), 28149 )
		self.assertEqual( len(obj["N"].data), 111930 )
		self.assertEqual( len(obj["uv"].data), 31402 )

	def testAttributes( self ) :

		node = AtomsGaffer.AtomsVariationReader()
		node["atomsVariationFile"].setValue( "${ATOMS_GAFFER_ROOT}/examples/assets/atomsRobot/atomsRobot.json" )

		attributes = node["out"].attributes( "/atomsRobot/Robot1/RobotSkin1/head/robot1_head" )
		self.assertTrue( "ai:polymesh:subdiv_adaptive_space" in attributes )
		self.assertEqual( attributes[ "ai:polymesh:subdiv_adaptive_space" ].value, "raster" )
		self.assertTrue( "ai:matte" in attributes )
		self.assertEqual( attributes[ "ai:matte" ].value, 0 )
		self.assertTrue( "ai:visibility:diffuse_reflection" in attributes )
		self.assertEqual( attributes[ "ai:visibility:diffuse_reflection" ].value, 1 )
		self.assertTrue( "jointIndexCount" in attributes )
		self.assertEqual( len( attributes["jointIndexCount"] ), 920 )
		self.assertTrue( "jointIndices" in attributes )
		self.assertEqual( len( attributes["jointIndices"] ), 920 )
		self.assertTrue( "jointWeights" in attributes )
		self.assertEqual( len( attributes["jointWeights"] ), 920 )

		attributes = node["out"].attributes( "/atomsRobot/Robot1/RobotSkin1/body/robot1_body" )
		self.assertTrue( "ai:polymesh:subdiv_adaptive_space" in attributes )
		self.assertEqual( attributes[ "ai:polymesh:subdiv_adaptive_space" ].value, "raster" )
		self.assertTrue( "ai:matte" in attributes )
		self.assertEqual( attributes[ "ai:matte" ].value, 0 )
		self.assertTrue( "ai:visibility:diffuse_reflection" in attributes )
		self.assertEqual( attributes[ "ai:visibility:diffuse_reflection" ].value, 1 )
		self.assertTrue( "jointIndexCount" in attributes )
		self.assertEqual( len( attributes["jointIndexCount"] ), 635 )
		self.assertTrue( "jointIndices" in attributes )
		self.assertEqual( len( attributes["jointIndices"] ), 1905 )
		self.assertTrue( "jointWeights" in attributes )
		self.assertEqual( len( attributes["jointWeights"] ), 1905 )
		self.assertEqual( attributes[ "user:atoms:fooBody" ].value, 1.5 )

		attributes = node["out"].attributes( "/atomsRobot/Robot1/RobotSkin1/arms/robot1_arms" )
		self.assertTrue( "ai:polymesh:subdiv_adaptive_space" in attributes )
		self.assertEqual( attributes[ "ai:polymesh:subdiv_adaptive_space" ].value, "raster" )
		self.assertTrue( "ai:matte" in attributes )
		self.assertEqual( attributes[ "ai:matte" ].value, 0 )
		self.assertTrue( "ai:visibility:diffuse_reflection" in attributes )
		self.assertEqual( attributes[ "ai:visibility:diffuse_reflection" ].value, 1 )
		self.assertTrue( "jointIndexCount" in attributes )
		self.assertEqual( len( attributes["jointIndexCount"] ), 960 )
		self.assertTrue( "jointIndices" in attributes )
		self.assertEqual( len( attributes["jointIndices"] ), 1600 )
		self.assertTrue( "jointWeights" in attributes )
		self.assertEqual( len( attributes["jointWeights"] ), 1600 )
		self.assertEqual( attributes[ "user:atoms:fooArm" ].value, 0.0 )

		attributes = node["out"].attributes( "/atomsRobot/Robot1/RobotSkin1/legs/robot1_legs" )
		self.assertTrue( "ai:polymesh:subdiv_adaptive_space" in attributes )
		self.assertEqual( attributes[ "ai:polymesh:subdiv_adaptive_space" ].value, "raster" )
		self.assertTrue( "ai:matte" in attributes )
		self.assertEqual( attributes[ "ai:matte" ].value, 0 )
		self.assertTrue( "ai:visibility:diffuse_reflection" in attributes )
		self.assertEqual( attributes[ "ai:visibility:diffuse_reflection" ].value, 1 )
		self.assertTrue( "jointIndexCount" in attributes )
		self.assertEqual( len( attributes["jointIndexCount"] ), 904 )
		self.assertTrue( "jointIndices" in attributes )
		self.assertEqual( len( attributes["jointIndices"] ), 1288 )
		self.assertTrue( "jointWeights" in attributes )
		self.assertEqual( len( attributes["jointWeights"] ), 1288 )

		attributes = node["out"].attributes( "/atomsRobot/Robot1:A/RobotSkin1/head/robot1_head" )
		self.assertTrue( "ai:polymesh:subdiv_adaptive_space" in attributes )
		self.assertEqual( attributes[ "ai:polymesh:subdiv_adaptive_space" ].value, "raster" )
		self.assertTrue( "ai:matte" in attributes )
		self.assertEqual( attributes[ "ai:matte" ].value, 0 )
		self.assertTrue( "ai:visibility:diffuse_reflection" in attributes )
		self.assertEqual( attributes[ "ai:visibility:diffuse_reflection" ].value, 1 )
		self.assertTrue( "jointIndexCount" in attributes )
		self.assertEqual( len( attributes["jointIndexCount"] ), 920 )
		self.assertTrue( "jointIndices" in attributes )
		self.assertEqual( len( attributes["jointIndices"] ), 920 )
		self.assertTrue( "jointWeights" in attributes )
		self.assertEqual( len( attributes["jointWeights"] ), 920 )

		attributes = node["out"].attributes( "/atomsRobot/Robot1:A/RobotSkin1/flag_group/pPlane1" )
		self.assertTrue( "ai:polymesh:subdiv_adaptive_space" in attributes )
		self.assertEqual( attributes[ "ai:polymesh:subdiv_adaptive_space" ].value, "raster" )
		self.assertTrue( "ai:matte" in attributes )
		self.assertEqual( attributes[ "ai:matte" ].value, 0 )
		self.assertTrue( "ai:visibility:diffuse_reflection" in attributes )
		self.assertEqual( attributes[ "ai:visibility:diffuse_reflection" ].value, 1 )
		self.assertFalse( "jointIndexCount" in attributes )
		self.assertFalse( "jointIndices" in attributes )
		self.assertFalse( "jointWeights" in attributes )


		attributes = node["out"].attributes( "/atomsRobot/Robot1:A/RobotSkin1/flag_group/pole" )
		self.assertTrue( "ai:polymesh:subdiv_adaptive_space" in attributes )
		self.assertEqual( attributes[ "ai:polymesh:subdiv_adaptive_space" ].value, "raster" )
		self.assertTrue( "ai:matte" in attributes )
		self.assertEqual( attributes[ "ai:matte" ].value, 0 )
		self.assertTrue( "ai:visibility:diffuse_reflection" in attributes )
		self.assertEqual( attributes[ "ai:visibility:diffuse_reflection" ].value, 1 )
		self.assertTrue( "jointIndexCount" in attributes )
		self.assertEqual( len( attributes["jointIndexCount"] ), 1022 )
		self.assertTrue( "jointIndices" in attributes )
		self.assertEqual( len( attributes["jointIndices"] ), 1022 )
		self.assertTrue( "jointWeights" in attributes )
		self.assertEqual( len( attributes["jointWeights"] ), 1022 )


		attributes = node["out"].attributes( "/atomsRobot/Robot1:A/RobotSkin1/body/robot1_body" )
		self.assertTrue( "ai:polymesh:subdiv_adaptive_space" in attributes )
		self.assertEqual( attributes[ "ai:polymesh:subdiv_adaptive_space" ].value, "raster" )
		self.assertTrue( "ai:matte" in attributes )
		self.assertEqual( attributes[ "ai:matte" ].value, 0 )
		self.assertTrue( "ai:visibility:diffuse_reflection" in attributes )
		self.assertEqual( attributes[ "ai:visibility:diffuse_reflection" ].value, 1 )
		self.assertTrue( "jointIndexCount" in attributes )
		self.assertEqual( len( attributes["jointIndexCount"] ), 635 )
		self.assertTrue( "jointIndices" in attributes )
		self.assertEqual( len( attributes["jointIndices"] ), 1905 )
		self.assertTrue( "jointWeights" in attributes )
		self.assertEqual( len( attributes["jointWeights"] ), 1905 )

		attributes = node["out"].attributes( "/atomsRobot/Robot1:B/RobotSkin1/body/robot1_body" )
		self.assertTrue( "ai:polymesh:subdiv_adaptive_space" in attributes )
		self.assertEqual( attributes[ "ai:polymesh:subdiv_adaptive_space" ].value, "raster" )
		self.assertTrue( "ai:matte" in attributes )
		self.assertEqual( attributes[ "ai:matte" ].value, 0 )
		self.assertTrue( "ai:visibility:diffuse_reflection" in attributes )
		self.assertEqual( attributes[ "ai:visibility:diffuse_reflection" ].value, 1 )
		self.assertTrue( "jointIndexCount" in attributes )
		self.assertEqual( len( attributes["jointIndexCount"] ), 635 )
		self.assertTrue( "jointIndices" in attributes )
		self.assertEqual( len( attributes["jointIndices"] ), 1905 )
		self.assertTrue( "jointWeights" in attributes )
		self.assertEqual( len( attributes["jointWeights"] ), 1905 )

		attributes = node["out"].attributes( "/atomsRobot/Robot2/robot2_head" )
		self.assertTrue( "ai:polymesh:subdiv_adaptive_space" in attributes )
		self.assertEqual( attributes[ "ai:polymesh:subdiv_adaptive_space" ].value, "raster" )
		self.assertTrue( "ai:matte" in attributes )
		self.assertEqual( attributes[ "ai:matte" ].value, 0 )
		self.assertTrue( "jointIndexCount" in attributes )
		self.assertEqual( len( attributes["jointIndexCount"] ), 5874 )
		self.assertTrue( "jointIndices" in attributes )
		self.assertEqual( len( attributes["jointIndices"] ), 5946 )
		self.assertTrue( "jointWeights" in attributes )
		self.assertEqual( len( attributes["jointWeights"] ), 5946 )

		attributes = node["out"].attributes( "/atomsRobot/Robot2/robot2_body" )
		self.assertTrue( "ai:polymesh:subdiv_adaptive_space" in attributes )
		self.assertEqual( attributes[ "ai:polymesh:subdiv_adaptive_space" ].value, "raster" )
		self.assertTrue( "ai:matte" in attributes )
		self.assertEqual( attributes[ "ai:matte" ].value, 0 )
		self.assertTrue( "jointIndexCount" in attributes )
		self.assertEqual( len( attributes["jointIndexCount"] ), 16944 )
		self.assertTrue( "jointIndices" in attributes )
		self.assertEqual( len( attributes["jointIndices"] ), 17693 )
		self.assertTrue( "jointWeights" in attributes )
		self.assertEqual( len( attributes["jointWeights"] ), 17693 )

		attributes = node["out"].attributes( "/atomsRobot/Robot2/robot2_arms" )
		self.assertTrue( "ai:polymesh:subdiv_adaptive_space" in attributes )
		self.assertEqual( attributes[ "ai:polymesh:subdiv_adaptive_space" ].value, "raster" )
		self.assertTrue( "ai:matte" in attributes )
		self.assertEqual( attributes[ "ai:matte" ].value, 0 )
		self.assertTrue( "jointIndexCount" in attributes )
		self.assertEqual( len( attributes["jointIndexCount"] ), 6288 )
		self.assertTrue( "jointIndices" in attributes )
		self.assertEqual( len( attributes["jointIndices"] ), 6391 )
		self.assertTrue( "jointWeights" in attributes )
		self.assertEqual( len( attributes["jointWeights"] ), 6391 )


		attributes = node["out"].attributes( "/atomsRobot/Robot2/robot2_legs" )
		self.assertTrue( "ai:polymesh:subdiv_adaptive_space" in attributes )
		self.assertEqual( attributes[ "ai:polymesh:subdiv_adaptive_space" ].value, "raster" )
		self.assertTrue( "ai:matte" in attributes )
		self.assertEqual( attributes[ "ai:matte" ].value, 0 )
		self.assertTrue( "jointIndexCount" in attributes )
		self.assertEqual( len( attributes["jointIndexCount"] ), 7200 )
		self.assertTrue( "jointIndices" in attributes )
		self.assertEqual( len( attributes["jointIndices"] ), 7200 )
		self.assertTrue( "jointWeights" in attributes )
		self.assertEqual( len( attributes["jointWeights"] ), 7200 )

		attributes = node["out"].attributes( "/atomsRobot/Robot2:A/robot2_head" )
		self.assertTrue( "ai:polymesh:subdiv_adaptive_space" in attributes )
		self.assertEqual( attributes[ "ai:polymesh:subdiv_adaptive_space" ].value, "raster" )
		self.assertTrue( "ai:matte" in attributes )
		self.assertEqual( attributes[ "ai:matte" ].value, 0 )
		self.assertTrue( "jointIndexCount" in attributes )
		self.assertEqual( len( attributes["jointIndexCount"] ), 5874 )
		self.assertTrue( "jointIndices" in attributes )
		self.assertEqual( len( attributes["jointIndices"] ), 5946 )
		self.assertTrue( "jointWeights" in attributes )
		self.assertEqual( len( attributes["jointWeights"] ), 5946 )


		attributes = node["out"].attributes( "/atomsRobot/Robot2:A/robot2_body" )
		self.assertTrue( "ai:polymesh:subdiv_adaptive_space" in attributes )
		self.assertEqual( attributes[ "ai:polymesh:subdiv_adaptive_space" ].value, "raster" )
		self.assertTrue( "ai:matte" in attributes )
		self.assertEqual( attributes[ "ai:matte" ].value, 0 )
		self.assertTrue( "jointIndexCount" in attributes )
		self.assertEqual( len( attributes["jointIndexCount"] ), 16944 )
		self.assertTrue( "jointIndices" in attributes )
		self.assertEqual( len( attributes["jointIndices"] ), 17693 )
		self.assertTrue( "jointWeights" in attributes )
		self.assertEqual( len( attributes["jointWeights"] ), 17693 )

		attributes = node["out"].attributes( "/atomsRobot/Robot2:B/robot2_body" )
		self.assertTrue( "ai:polymesh:subdiv_adaptive_space" in attributes )
		self.assertEqual( attributes[ "ai:polymesh:subdiv_adaptive_space" ].value, "raster" )
		self.assertTrue( "ai:matte" in attributes )
		self.assertEqual( attributes[ "ai:matte" ].value, 0 )
		self.assertTrue( "jointIndexCount" in attributes )
		self.assertEqual( len( attributes["jointIndexCount"] ), 16944 )
		self.assertTrue( "jointIndices" in attributes )
		self.assertEqual( len( attributes["jointIndices"] ), 17693 )
		self.assertTrue( "jointWeights" in attributes )
		self.assertEqual( len( attributes["jointWeights"] ), 17693 )

		attributes = node["out"].attributes( "/atoms2Robot/YellowRobot/Body/RobotBody" )
		self.assertTrue( "ai:polymesh:subdiv_adaptive_space" in attributes )
		self.assertEqual( attributes[ "ai:polymesh:subdiv_adaptive_space" ].value, "raster" )
		self.assertTrue( "ai:matte" in attributes )
		self.assertEqual( attributes[ "ai:matte" ].value, 0 )
		self.assertTrue( "ai:visibility:diffuse_reflection" in attributes )
		self.assertEqual( attributes[ "ai:visibility:diffuse_reflection" ].value, 1 )
		self.assertTrue( "jointIndexCount" in attributes )
		self.assertEqual( len( attributes["jointIndexCount"] ), 28149 )
		self.assertTrue( "jointIndices" in attributes )
		self.assertEqual( len( attributes["jointIndices"] ), 40309 )
		self.assertTrue( "jointWeights" in attributes )
		self.assertEqual( len( attributes["jointWeights"] ), 40309 )

		attributes = node["out"].attributes( "/atoms2Robot/RedRobot/Body/RobotBody" )
		self.assertTrue( "ai:polymesh:subdiv_adaptive_space" in attributes )
		self.assertEqual( attributes[ "ai:polymesh:subdiv_adaptive_space" ].value, "raster" )
		self.assertTrue( "ai:matte" in attributes )
		self.assertEqual( attributes[ "ai:matte" ].value, 0 )
		self.assertTrue( "ai:visibility:diffuse_reflection" in attributes )
		self.assertEqual( attributes[ "ai:visibility:diffuse_reflection" ].value, 1 )
		self.assertTrue( "jointIndexCount" in attributes )
		self.assertEqual( len( attributes["jointIndexCount"] ), 28149 )
		self.assertTrue( "jointIndices" in attributes )
		self.assertEqual( len( attributes["jointIndices"] ), 40309 )
		self.assertTrue( "jointWeights" in attributes )
		self.assertEqual( len( attributes["jointWeights"] ), 40309 )

		attributes = node["out"].attributes( "/atoms2Robot/RedRobot:A/Body/RobotBody" )
		self.assertTrue( "ai:polymesh:subdiv_adaptive_space" in attributes )
		self.assertEqual( attributes[ "ai:polymesh:subdiv_adaptive_space" ].value, "raster" )
		self.assertTrue( "ai:matte" in attributes )
		self.assertEqual( attributes[ "ai:matte" ].value, 0 )
		self.assertTrue( "ai:visibility:diffuse_reflection" in attributes )
		self.assertEqual( attributes[ "ai:visibility:diffuse_reflection" ].value, 1 )
		self.assertTrue( "jointIndexCount" in attributes )
		self.assertEqual( len( attributes["jointIndexCount"] ), 28149 )
		self.assertTrue( "jointIndices" in attributes )
		self.assertEqual( len( attributes["jointIndices"] ), 40309 )
		self.assertTrue( "jointWeights" in attributes )
		self.assertEqual( len( attributes["jointWeights"] ), 40309 )

		attributes = node["out"].attributes( "/atoms2Robot/PurpleRobot/Body/RobotBody" )
		self.assertTrue( "ai:polymesh:subdiv_adaptive_space" in attributes )
		self.assertEqual( attributes[ "ai:polymesh:subdiv_adaptive_space" ].value, "raster" )
		self.assertTrue( "ai:matte" in attributes )
		self.assertEqual( attributes[ "ai:matte" ].value, 0 )
		self.assertTrue( "ai:visibility:diffuse_reflection" in attributes )
		self.assertEqual( attributes[ "ai:visibility:diffuse_reflection" ].value, 1 )
		self.assertTrue( "jointIndexCount" in attributes )
		self.assertEqual( len( attributes["jointIndexCount"] ), 28149 )
		self.assertTrue( "jointIndices" in attributes )
		self.assertEqual( len( attributes["jointIndices"] ), 40309 )
		self.assertTrue( "jointWeights" in attributes )
		self.assertEqual( len( attributes["jointWeights"] ), 40309 )

		attributes = node["out"].attributes( "/atomsRobot/Robot1/RobotSkin1/flag_group" )
		self.assertEqual( attributes[ "user:atoms:fooFlagGroup" ].value, imath.V3f( 1.0, 2.0, 3.0) )

	def testTransform( self ) :
		node = AtomsGaffer.AtomsVariationReader()
		node["atomsVariationFile"].setValue( "${ATOMS_GAFFER_ROOT}/examples/assets/atomsRobot/atomsRobot.json" )

		obj = node["out"].transform( "/atomsRobot/Robot1" )
		self.assertEqual( obj, imath.M44f() )

		obj = node["out"].transform( "/atomsRobot/Robot1/RobotSkin1" )
		self.assertEqual( obj, imath.M44f() )

		obj = node["out"].transform( "/atomsRobot/Robot1/RobotSkin1/head" )
		self.assertEqual( obj, imath.M44f( 1, 0, 0, 0, 0, 0.995992899, 0.0894325897, 0, 0, -0.0894325897, 0.995992899, 0, 0, 1.03006685, -4.52774239, 1 ) )

		obj = node["out"].transform( "/atomsRobot/Robot1/RobotSkin1/head/robot1_head" )
		self.assertEqual( obj, imath.M44f().translate( imath.V3f( 0.0, 51.0, 0.0 ) ) )

		obj = node["out"].transform( "/atomsRobot/Robot1/RobotSkin1/arms" )
		self.assertEqual( obj, imath.M44f().translate( imath.V3f( 0.0, 13.1848993, 0.0 ) ) )

		obj = node["out"].transform( "/atomsRobot/Robot1/RobotSkin1/arms/robot1_arms" )
		self.assertEqual( obj, imath.M44f().translate( imath.V3f( 0.0, 15.8421688, 0.0 ) ) )

		obj = node["out"].transform( "/atomsRobot/Robot1/RobotSkin1/body" )
		self.assertEqual( obj, imath.M44f() )

		obj = node["out"].transform( "/atomsRobot/Robot1/RobotSkin1/body/robot1_body" )
		self.assertEqual( obj, imath.M44f().translate( imath.V3f( 0.0, 16.0, 0.0 ) ) )

		obj = node["out"].transform( "/atomsRobot/Robot1/RobotSkin1/legs" )
		self.assertEqual( obj, imath.M44f().translate( imath.V3f( 0.0, -10.0, 0.0 ) ) )

		obj = node["out"].transform( "/atomsRobot/Robot1/RobotSkin1/legs/robot1_legs" )
		self.assertEqual( obj, imath.M44f().translate( imath.V3f( 0.0, -33.0, 0.0 ) ) )

		obj = node["out"].transform( "/atomsRobot/Robot1/RobotSkin1/flag_group" )
		self.assertEqual( obj.translation(), imath.V3f( 75.4688797, 28.3711166, 11.6567278 ) )

		obj = node["out"].transform( "/atomsRobot/Robot1/RobotSkin1/flag_group/pPlane1" )
		self.assertEqual( obj, imath.M44f( 64.4932404, 0, 0, 0, 0, 64.4932404, 0, 0, 0, 0, 41.1785202, 0, -32.3346634, 0, 94.8534851, 1 ) )

		obj = node["out"].transform( "/atomsRobot/Robot1/RobotSkin1/flag_group/pole" )
		self.assertEqual( obj, imath.M44f() )

	def testSets( self ):
		node = AtomsGaffer.AtomsVariationReader()
		node["atomsVariationFile"].setValue( "${ATOMS_GAFFER_ROOT}/examples/assets/atomsRobot/atomsRobot.json" )

		obj = node["out"]
		set_names = obj["setNames"].getValue()

		self.assertTrue( "atoms2Robot:PurpleRobot" in set_names )
		self.assertEqual(
			set( obj.set( "atoms2Robot:PurpleRobot" ).value.paths() ),
			{
				"/atoms2Robot/PurpleRobot/Body/RobotBody"
			}
		)

		self.assertTrue( "atoms2Robot:RedRobot" in set_names )
		self.assertEqual(
			set( obj.set( "atoms2Robot:RedRobot" ).value.paths() ),
			{
				"/atoms2Robot/RedRobot/Body/RobotBody"
			}
		)
		#print node["out"].set( "atoms2Robot:RedRobot" ).value.paths()

		self.assertTrue( "atoms2Robot:RedRobot:A" in set_names )
		self.assertEqual(
			set( obj.set( "atoms2Robot:RedRobot:A" ).value.paths() ),
			{
				"/atoms2Robot/RedRobot:A/Body/RobotBody"
			}
		)

		self.assertTrue( "atoms2Robot:YellowRobot" in set_names )
		self.assertEqual(
			set( obj.set( "atoms2Robot:YellowRobot" ).value.paths() ),
			{
				"/atoms2Robot/YellowRobot/Body/RobotBody"
			}
		)

		self.assertTrue( "atomsRobot:Robot1" in set_names )

		self.assertEqual(
			set( obj.set( "atomsRobot:Robot1" ).value.paths() ),
			{
				'/atomsRobot/Robot1/RobotSkin1/head/robot1_head',
				'/atomsRobot/Robot1/RobotSkin1/arms/robot1_arms',
				'/atomsRobot/Robot1/RobotSkin1/legs/robot1_legs',
				'/atomsRobot/Robot1/RobotSkin1/flag_group/pole',
				'/atomsRobot/Robot1/RobotSkin1/flag_group/pPlane1',
				'/atomsRobot/Robot1/RobotSkin1/body/robot1_body'
			}
		)

		self.assertTrue( "atomsRobot:Robot1:A" in set_names )
		self.assertEqual(
			set( obj.set( "atomsRobot:Robot1:A" ).value.paths() ),
			{
				'/atomsRobot/Robot1:A/RobotSkin1/head/robot1_head',
				'/atomsRobot/Robot1:A/RobotSkin1/body/robot1_body'
			}
		)


		self.assertTrue( "atomsRobot:Robot1:B" in set_names )
		self.assertEqual(
			set( obj.set( "atomsRobot:Robot1:B" ).value.paths() ),
			{
				'/atomsRobot/Robot1:B/RobotSkin1/body/robot1_body'
			}
		)


		self.assertTrue( "atomsRobot:Robot2" in set_names )
		self.assertEqual(
			set( obj.set( "atomsRobot:Robot2" ).value.paths() ),
			{
				'/atomsRobot/Robot2/robot2_arms',
				'/atomsRobot/Robot2/robot2_body',
				'/atomsRobot/Robot2/robot2_head',
				'/atomsRobot/Robot2/robot2_legs'
			}
		)


		self.assertTrue( "atomsRobot:Robot2:A" in set_names )
		self.assertEqual(
			set( obj.set( "atomsRobot:Robot2:A" ).value.paths() ),
			{
				'/atomsRobot/Robot2:A/robot2_body',
				'/atomsRobot/Robot2:A/robot2_head'
			}
		)

		self.assertTrue( "atomsRobot:Robot2:B" in set_names )
		self.assertEqual(
			set( obj.set( "atomsRobot:Robot2:B" ).value.paths() ),
			{
				'/atomsRobot/Robot2:B/robot2_body'
			}
		)

		self.assertTrue( "armsSet" in set_names )
		self.assertEqual(
			set( obj.set( "armsSet" ).value.paths() ),
			{
				'/atomsRobot/Robot1/RobotSkin1/arms/robot1_arms'
			}
		)

		self.assertTrue( "robotSet" in set_names )
		self.assertEqual(
			set( obj.set( "robotSet" ).value.paths() ),
			{
				'/atomsRobot/Robot1:A/RobotSkin1/head/robot1_head',
				'/atomsRobot/Robot1:A/RobotSkin1/body/robot1_body',
				'/atomsRobot/Robot1:B/RobotSkin1/body/robot1_body',
				'/atomsRobot/Robot1/RobotSkin1/head/robot1_head',
				'/atomsRobot/Robot1/RobotSkin1/legs/robot1_legs',
				'/atomsRobot/Robot1/RobotSkin1/arms/robot1_arms',
				'/atomsRobot/Robot1/RobotSkin1/body/robot1_body'
			}
		)

		self.assertTrue( "bodySet" in set_names )
		self.assertEqual(
			set( obj.set( "bodySet" ).value.paths() ),
			{
				'/atomsRobot/Robot1:A/RobotSkin1/body/robot1_body',
				'/atomsRobot/Robot1:B/RobotSkin1/body/robot1_body',
				'/atomsRobot/Robot1/RobotSkin1/body/robot1_body'
			}
		)

		self.assertTrue( "initialShadingGroup" in set_names )
		self.assertEqual(
		set( obj.set( "initialShadingGroup" ).value.paths() ),
			{
				'/atomsRobot/Robot1/RobotSkin1/flag_group/pPlane1'
			}
		)

		self.assertTrue( "phong3SG" in set_names )
		self.assertEqual(
			set( obj.set( "phong3SG" ).value.paths() ),
			{
				'/atomsRobot/Robot1/RobotSkin1/flag_group/pole'
			}
		)

		self.assertTrue( "headSet" in set_names )
		self.assertEqual(
			set( obj.set( "headSet" ).value.paths() ),
			{
				'/atomsRobot/Robot1:A/RobotSkin1/head/robot1_head',
				'/atomsRobot/Robot1/RobotSkin1/head/robot1_head'
			}
		)

		self.assertTrue( "legsSet" in set_names )
		self.assertEqual(
			set( obj.set( "legsSet" ).value.paths() ),
			{
				'/atomsRobot/Robot1/RobotSkin1/legs/robot1_legs'
			}
		)

		self.assertTrue( "fooSet" in set_names )
		self.assertEqual(
			set( obj.set( "fooSet" ).value.paths() ),
			{
				'/atomsRobot/Robot1/RobotSkin1/legs/robot1_legs'
			}
		)

		self.assertTrue( "newFooSet" in set_names )
		self.assertEqual(
			set( obj.set( "newFooSet" ).value.paths() ),
			{
				'/atomsRobot/Robot1/RobotSkin1/legs/robot1_legs'
			}
		)


if __name__ == "__main__":
	unittest.main()
