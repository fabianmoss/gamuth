\paper {

evenFooterMarkup = ##f

oddFooterMarkup = ##f
}
\version "2.20.0"
\header {

tagline = ##f
}
\score {
<<
   \new Staff \relative c' {
   \tempo 4 = 120
      c4 cis d ees e f fis g aes a bes b
}
>>

\layout {}

\midi {}
}