import React from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { motion } from "framer-motion";

const mockData = [
  {
    id: 1,
    title: "Project Alpha Meeting",
    transcripts: 5,
    actionItems: 12,
    sentiment: "Positive",
  },
  {
    id: 2,
    title: "Client Sync - Beta",
    transcripts: 3,
    actionItems: 7,
    sentiment: "Neutral",
  },
  {
    id: 3,
    title: "Internal Review",
    transcripts: 8,
    actionItems: 20,
    sentiment: "Negative",
  },
];

export default function Dashboard() {
  return (
    <div className="p-6 grid gap-6">
      <h1 className="text-2xl font-bold">Dashboard</h1>

      {/* Summary Section */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <Card className="rounded-2xl shadow">
          <CardContent className="p-4">
            <p className="text-sm">Total Meetings</p>
            <h2 className="text-xl font-semibold">{mockData.length}</h2>
          </CardContent>
        </Card>

        <Card className="rounded-2xl shadow">
          <CardContent className="p-4">
            <p className="text-sm">Total Transcripts</p>
            <h2 className="text-xl font-semibold">
              {mockData.reduce((acc, m) => acc + m.transcripts, 0)}
            </h2>
          </CardContent>
        </Card>

        <Card className="rounded-2xl shadow">
          <CardContent className="p-4">
            <p className="text-sm">Total Action Items</p>
            <h2 className="text-xl font-semibold">
              {mockData.reduce((acc, m) => acc + m.actionItems, 0)}
            </h2>
          </CardContent>
        </Card>
      </div>

      {/* Meetings List */}
      <div className="grid gap-4">
        {mockData.map((meeting) => (
          <motion.div
            key={meeting.id}
            whileHover={{ scale: 1.02 }}
            className=""
          >
            <Card className="rounded-2xl shadow">
              <CardContent className="p-4 flex justify-between items-center">
                <div>
                  <h3 className="text-lg font-semibold">{meeting.title}</h3>
                  <p className="text-sm text-gray-500">
                    Transcripts: {meeting.transcripts} | Action Items: {meeting.actionItems}
                  </p>
                  <p className="text-sm">Sentiment: {meeting.sentiment}</p>
                </div>
                <Button>View Details</Button>
              </CardContent>
            </Card>
          </motion.div>
        ))}
      </div>
    </div>
  );
}
