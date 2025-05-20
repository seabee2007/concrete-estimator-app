import React from 'react';
import { SafeAreaView, StatusBar, ScrollView, View, Text } from 'react-native';
import EstimateScreen from './components/EstimateScreen';

export default function App() {
  return (
    <SafeAreaView style={{ flex: 1, backgroundColor: '#f7fafc' }}>
      <StatusBar barStyle="dark-content" />
      <ScrollView contentContainerStyle={{ padding: 16 }}>
        <Text style={{ fontSize: 24, fontWeight: 'bold', marginBottom: 12 }}>
          Concrete Estimator
        </Text>
        <EstimateScreen />
      </ScrollView>
    </SafeAreaView>
  );
}
