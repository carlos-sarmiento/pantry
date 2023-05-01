'use client'

import React from 'react';
import Nav from 'react-bootstrap/Nav';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import VerticalDivider from '@/layout/VerticalDivider';
import LayoutNavigationSidebar from '@/layout/LayoutNavigationSidebar';
import DebuggingCard from '@/utilities/DebugWindow';

export default function Home() {
  return (
    <>
      <DebuggingCard label="Test" value={{ val: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Praesent tristique magna sit amet purus gravida quis blandit turpis. Vel quam elementum pulvinar etiam non quam lacus suspendisse faucibus. Quis viverra nibh cras pulvinar. Etiam erat velit scelerisque in dictum non. Imperdiet dui accumsan sit amet nulla facilisi morbi tempus iaculis. Arcu cursus euismod quis viverra. Vitae nunc sed velit dignissim sodales ut eu. Elit duis tristique sollicitudin nibh sit amet commodo nulla. Massa vitae tortor condimentum lacinia quis vel. Faucibus vitae aliquet nec ullamcorper sit amet risus nullam. Adipiscing diam donec adipiscing tristique risus nec feugiat. Facilisis mauris sit amet massa vitae tortor. Sed blandit libero volutpat sed cras ornare arcu. Dui nunc mattis enim ut tellus elementum sagittis vitae. Quisque egestas diam in arcu cursus euismod. Ut placerat orci nulla pellentesque. Sed arcu non odio euismod lacinia. Mauris pharetra et ultrices neque ornare. A erat nam at lectus." }} />
    </>
  )
}
