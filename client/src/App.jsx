import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Dashboard from './features/caregiver/Dashboard'
import ModeSelect from './features/onboarding/ModeSelect'
import PainBoard from './features/pain/PainBoard'
import StoryGenerator from './features/stories/StoryGenerator'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<ModeSelect />} />
        <Route path="/pain" element={<PainBoard />} />
        <Route path="/caregiver" element={<Dashboard />} />
        <Route path="/stories" element={<StoryGenerator />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
