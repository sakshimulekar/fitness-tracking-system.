import { View, Text } from 'react-native'
import React from 'react'
import { NavigationContainer } from '@react-navigation/native'
import { createStackNavigator } from '@react-navigation/stack'
import HomeScreen from './Screens/HomeScreen'
import UserProfile from './Screens/UserProfile'
import UserProfileForm from './Screens/UserProfileForm'
import WorkOutScreen from './Screens/WorkOutScreen'
import FitScreen from './Screens/FitScreen'
import RestScreen from './Screens/RestScreen'


const Stack = createStackNavigator()

export default function AppNavigator() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Home" component={HomeScreen} options={{headerShown:false}}/>
        <Stack.Screen name='UserProfile' component={UserProfile}/>
        <Stack.Screen name='UserProfileForm' component={UserProfileForm}/>
        <Stack.Screen name='workout' component={WorkOutScreen} options={{headerShown:false}}/>
        <Stack.Screen name='fit' component={FitScreen} options={{headerShown:false}}/>
        <Stack.Screen name='rest' component={RestScreen} options={{headerShown:false}}/>
      </Stack.Navigator>
    </NavigationContainer>
  )
}