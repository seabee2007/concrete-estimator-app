// frontend/mobile/App.js
import React from 'react';
import { SafeAreaView, StatusBar, Text } from 'react-native';
import EstimateScreen from './components/EstimateScreen';

export default function App() {
  return (
    <SafeAreaView style={{ flex: 1, backgroundColor: '#f7fafc' }}>
      <StatusBar barStyle="dark-content" />
      <EstimateScreen />
    </SafeAreaView>
  );
}
