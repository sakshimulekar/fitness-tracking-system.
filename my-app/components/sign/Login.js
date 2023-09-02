import { View, Text,TextInput,Button,Alert } from 'react-native'
import React, { useState } from 'react'
import axios from 'axios'

export default function Login() {
  const [email,setEmail] = useState("")
  const [password,setPassword] = useState("")

  const validateForm = () => {
    if ( !email || !password  ) {
      Alert.alert('Validation Error', 'All fields are required');
      return false;
    }
    return true;
  };
    
  const handlePress = () => {
    if (!validateForm()) {
      return; // Stop the submission if validation fails
    }
  
    axios.post("http://127.0.0.1:8000/api/login/",{email,password})
    .then((res)=>{
      console.log(res.data)
      Alert.alert('Success', 'Login successful', [
        {
          text: 'OK',
          onPress: () => {
            // Reset the form fields after successful login
            setName('');
            setEmail('');
            setPassword('');
            setUsername('');
            setIsTrainer(false);
          },
        },
      ]);
    })
    .catch(err=>{
      console.log(err.message)
      Alert.alert('Error', 'Login failed');
    })
  }
  return (
    <View>
      <Text>Login Form</Text>
      <TextInput
        placeholder="Enter Email"
        value={email}
        onChangeText={(text)=>setEmail(text)}
      />
      <TextInput
        placeholder="Enter Password"
        value={password}
        onChangeText={(text)=>setPassword(text)}
      />
      <Button title="Log In" onPress={handlePress}/>
    </View>
  )
}