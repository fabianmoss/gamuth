% add to all score examples
%%%%%%%%%%%%%%%%%%%%%%%%%%%
#(set-global-staff-size 20)
\include "lilypond-book-preamble.ly"
\paper { oddFooterMarkup = ##f }
% remove footer
\header {
  tagline = ""
}
%%%%%%%%%%%%%%%%%%%%%%%%%%%

\score{
      
      \relative c' {
      \time 12/4
      \tempo 4 = 120
      \hide Score.MetronomeMark
      \override Score.TimeSignature.stencil = ##f
      c4 cis d ees e f fis g aes a bes b
}
}
