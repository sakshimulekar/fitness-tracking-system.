import React from 'react';
import AppNavigator from './AppNavigator';
import { FitnessContext } from './Context';
import SignUp from './components/sign/SignUp';
import Login from './components/sign/Login';


export default function App() {
  return (
    <FitnessContext>
      <SignUp/>
      <Login/>
    {/* <AppNavigator /> */}
    </FitnessContext>
  );
}
