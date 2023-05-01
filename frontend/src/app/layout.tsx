// "use client";

import './globals.css'
import '../fontawesome/css/fontawesome.css'
import { Inter } from 'next/font/google'
import 'bootstrap/dist/css/bootstrap.css';
import CoreChrome from '@/CoreChrome';

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'Pantry',
  description: 'Pantry - Keep an eye on your stuff',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
        <link
          rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" />
      </head>
      <body className={inter.className} style={{ "height": "100vh", width: "100vw" }}>
        <CoreChrome>
          {children}
        </CoreChrome>
      </body>
    </html>
  )
}