<script type='text/javascript'>

  var image_deg    = new Array();
  var image_scale  = new Array();
  var image_factor = new Array();
  var image_W      = new Array();
  var image_H      = new Array();
  var view_W       = new Array();
  var view_H       = new Array();

  function show_image(num, scale, force_width, force_height)
  {
      var image   = document.getElementById('I' + num + '_image');
      var canvas  = document.getElementById('I' + num + '_canvas');
      var percent = document.getElementById('I' + num + '_percent');
      var area    = document.getElementById('I' + num + '_area');

      if (scale == null) {
          image_factor[num] = 1
          image.width       = view_W[num];
          image.height      = view_H[num];
      } else if (scale != 1) {
          image_factor[num] *= scale;
          image.width       *= scale;
          image.height      *= scale;
      }


      if (typeof(canvas.getContext) == "function")
      {
          var canvasContext = canvas.getContext('2d');

          switch(image_deg[num]) {
              default :
                canvas.style.display = 'none';
                image.style.display = 'inline';
                break;

              case 90:
                canvas.setAttribute('width',  image.height);
                canvas.setAttribute('height', image.width);
                canvasContext.rotate(90 * Math.PI / 180);
                canvasContext.drawImage(image, 0, -image.height, image.width, image.height);
                image.style.display = 'none';
                canvas.style.display = 'inline';
                break;

              case 180:
                canvas.setAttribute('width',  image.width);
                canvas.setAttribute('height', image.height);
                canvasContext.rotate(180 * Math.PI / 180);
                canvasContext.drawImage(image, -image.width, -image.height, image.width, image.height);
                image.style.display = 'none';
                canvas.style.display = 'inline';
                break;

              case 270:
                canvas.setAttribute('width', image.height);
                canvas.setAttribute('height', image.width);
                canvasContext.rotate(270 * Math.PI / 180);
                canvasContext.drawImage(image, -image.width, 0, image.width, image.height);
                image.style.display = 'none';
                canvas.style.display = 'inline';
                break;
          }
      }
      else
      {
          switch(image_deg[num]) {
              default:
                    image.style.filter = 'progid:DXImageTransform.Microsoft.BasicImage(rotation=0)';
                    break;

              case 90:
                    image.style.filter = 'progid:DXImageTransform.Microsoft.BasicImage(rotation=1)';
                    break;

              case 180:
                    image.style.filter = 'progid:DXImageTransform.Microsoft.BasicImage(rotation=2)';
                    break;

              case 270:
                    image.style.filter = 'progid:DXImageTransform.Microsoft.BasicImage(rotation=3)';
                    break;
          }
      }

      percent.innerHTML = Math.round(image_factor[num] * 100) + "%";
      if (area && image_W[num] && image_H[num])
      {
          area.innerHTML = Math.round(image.width * image.height  / (image_W[num] * image_H[num]) * 100) + "%";
      }
  }

  function zoom_image(num, dir)
  {

      if (dir > 0)
         show_image(num, 1.25);
      else
         show_image(num,  .75);
  }

  function rotate_image(num, dir)
  {
      image_deg[num] += 90 * dir;
      if ((image_deg[num] <= 0) || (image_deg[num] >= 360))
          image_deg[num] = 0;

      show_image(num, 1);
  }

</script>

<title>Jeffrey's Exif viewer</title>
<style>
a.quiet:visited, a.quiet:link {
  text-decoration: none;
}
a.quiet:hover {
  text-decoration: underline;
}
</style>
<div style='float:right;
     background-color: #FDD;
     border-right: 1px solid #EEE;
     border-left: 1px solid #EEE;
     border-bottom: 1px solid #EEE;
     padding: 5px 5px 5px 5px'>
<center>
   <big><b><a href='http://regex.info/blog/' style='text-decoration: none'>Jeffrey's</a> Exif Viewer</b></big>
   <br><small>(<a href='http://regex.info/blog/other-writings/online-exif-image-data-viewer/'>help</a>)</small>

    <p><table width="300" style="background-color: #FEE; border: solid 1px gray; padding: 5px">
    <tr><td>
    <font style="font-size: 85%">Note: extra functionality is enabled when you use <a href="http://www.mozilla.com/firefox/">Firefox</a> or another <a href='http://en.wikipedia.org/wiki/Gecko_%28layout_engine%29'>Gecko</a>-based browser..
    </font></td></tr></table></p>
        

<table width="300" style="background-color: #FEE; border: solid 1px gray; margin-top: 5px">
<tr><td>
<font style="font-size: 90%">
<b>Some of my other stuff</b>
<br/>
<span style='white-space:nowrap'>&middot;&nbsp; <a class='quiet' href='http://regex.info/blog/'>My Blog</a>&nbsp;</span>
<span style='white-space:nowrap'>&middot;&nbsp; <a class='quiet' href='http://regex.info/blog/category/camera-equipment/'>&#8220;Camera Stuff&#8221;</a>&nbsp;</span>
<span style='white-space:nowrap'>&middot;&nbsp; <a class='quiet' href='http://regex.info/blog/photo-tech/'>&#8220;Photo Tech&#8221;</a>&nbsp;</span>
<span style='white-space:nowrap'>&middot;&nbsp; <a class='quiet' href='http://regex.info/blog/category/pretty-photos/desktop-backgrounds/'>Desktop Backgrounds</a>&nbsp;</span>
<span style='white-space:nowrap'>&middot;&nbsp; <a class='quiet' href='http://regex.info/blog/category/pretty-photos/'>Pretty Photos</a>&nbsp;</span>
</font></td></tr></table>

</center></div>


<table><tr><td>
check a file on the web...
<form style='border: 1px solid gray; padding: 5px' action='exif.cgi'>Image <b>URL</b>: <input name='url' size='30'/>
&nbsp;&nbsp;&nbsp; <input  style='font-size: 80%'  type='submit' value='View Image At Url'/>
</form>

or check a file on your local disk...

<form style='border: 1px solid gray; padding: 5px' action='exif.cgi' method='post' enctype='multipart/form-data' accept='image/*'>
Local Image <b>File</b>: <input type='file' name='f' accept='image/*'/>
&nbsp;&nbsp;&nbsp; <input style='font-size: 80%' type='submit' value='View Image From File'/></form>

</td></tr></table>
<b>Works with these file types</b>: <span style='font-size: 80%'>3FR, 3G2, 3GP, ACFM, <span title="ACR: American College of Radiology ACR-NEMA">ACR</span>, AFM, <span title="AI: Adobe Illustrator (PDF-like or PS-like)">AI</span>, <span title="AIF: Audio Interchange File Format (.3)">AIF</span>, <span title="AIFC: Audio Interchange File Format Compressed">AIFC</span>, <span title="AIFF: Audio Interchange File Format (.4)">AIFF</span>, AMFM, APE, ARW, <span title="ASF: Microsoft Advanced Systems Format">ASF</span>, <span title="AVI: Audio Video Interleaved (RIFF-based)">AVI</span>, <span title="BMP: Windows BitMaP">BMP</span>, BTF, CIFF, COS, <b style='font-size:120%'><span title="CR2: Canon RAW 2 format (TIFF-like)">CR2</span></b>, <b style='font-size:120%'><span title="CRW: Canon RAW format">CRW</span></b>, CS1, <span title="DC3: DICOM image file">DC3</span>, <span title="DCM: DICOM image file">DCM</span>, DCP, DCR, DFONT, <span title="DIB: Device Independent Bitmap (aka. BMP)">DIB</span>, <span title="DIC: DICOM image file">DIC</span>, <span title="DICM: DICOM image file">DICM</span>, DIVX, DJV, DJVU, DLL, <b style='font-size:120%'><span title="DNG: Digital Negative (TIFF-like)">DNG</span></b>, DOC, DOCM, DOCX, DOT, DOTM, DOTX, DVB, DYLIB, EIP, <span title="EPS: Encapsulated PostScript Format (.3)">EPS</span>, <span title="EPSF: Encapsulated PostScript Format (.4)">EPSF</span>, <span title="ERF: Epson Raw Format (TIFF-like)">ERF</span>, EXE, EXIF, F4A, F4B, F4P, F4V, FLA, FLAC, FLV, <span title="FPX: FlashPix">FPX</span>, <span title="GIF: Compuserve Graphics Interchange Format">GIF</span>, GZ, GZIP, HDP, HTM, HTML, <span title="ICC: International Color Consortium">ICC</span>, <span title="ICM: International Color Consortium">ICM</span>, IIQ, IND, INDD, INDT, ITC, <span title="JNG: JPG Network Graphics (PNG-like)">JNG</span>, <span title="JP2: JPEG 2000 file">JP2</span>, <span title="JPEG: Joint Photographic Experts Group (.4)">JPEG</span>, <b style='font-size:120%'><span title="JPG: Joint Photographic Experts Group (.3)">JPG</span></b>, JPM, <span title="JPX: JPEG 2000 file">JPX</span>, K25, KDC, KEY, KTH, LNK, M2T, M2TS, M2V, M4A, M4B, M4P, M4V, MEF, <span title="MIE: Meta Information Encapsulation format">MIE</span>, <span title="MIF: Magick Image File Format (.3)">MIF</span>, <span title="MIFF: Magick Image File Format (.4)">MIFF</span>, MKA, MKS, MKV, <span title="MNG: Multiple-image Network Graphics (PNG-like)">MNG</span>, <span title="MOS: Creo Leaf Mosaic (TIFF-like)">MOS</span>, <span title="MOV: Apple QuickTime movie">MOV</span>, <span title="MP3: MPEG Layer 3 audio (uses ID3 information)">MP3</span>, <span title="MP4: MPEG Layer 4 video (QuickTime-based)">MP4</span>, MPC, <span title="MPEG: MPEG audio/video format 1">MPEG</span>, <span title="MPG: MPEG audio/video format 1">MPG</span>, MPO, MQV, <span title="MRW: Minolta RAW format">MRW</span>, MTS, <b style='font-size:120%'><span title="NEF: Nikon (RAW) Electronic Format (TIFF-like)">NEF</span></b>, NMBTEMPLATE, NRW, NUMBERS, ODP, ODS, ODT, OGG, <span title="ORF: Olympus RAW format">ORF</span>, OTF, PAGES, <span title="PBM: Portable BitMap (PPM-like)">PBM</span>, <span title="PCT: Apple PICTure (.3)">PCT</span>, <span title="PDF: Adobe Portable Document Format">PDF</span>, <span title="PEF: Pentax (RAW) Electronic Format (TIFF-like)">PEF</span>, PFA, PFB, PFM, <span title="PGM: Portable Gray Map (PPM-like)">PGM</span>, <span title="PICT: Apple PICTure (.4)">PICT</span>, PMP, <b style='font-size:120%'><span title="PNG: Portable Network Graphics">PNG</span></b>, POT, POTM, POTX, <span title="PPM: Portable Pixel Map">PPM</span>, PPS, PPSM, PPSX, PPT, PPTM, PPTX, <span title="PS: PostScript">PS</span>, PSB, <span title="PSD: PhotoShop Drawing">PSD</span>, PSP, PSPFRAME, PSPIMAGE, PSPSHAPE, PSPTUBE, <span title="QIF: QuickTime Image File (.3 alternate)">QIF</span>, <span title="QT: QuickTime movie">QT</span>, <span title="QTI: QuickTime Image File (.3)">QTI</span>, <span title="QTIF: QuickTime Image File (.4)">QTIF</span>, <span title="RA: Real Audio">RA</span>, <span title="RAF: FujiFilm RAW Format">RAF</span>, <span title="RAM: Real Audio Metafile">RAM</span>, <b style='font-size:120%'><span title="RAW: Kyocera Contax N Digital RAW or Panasonic RAW">RAW</span></b>, <span title="RIF: Resource Interchange File Format (.3)">RIF</span>, <span title="RIFF: Resource Interchange File Format (.4)">RIFF</span>, <span title="RM: Real Media">RM</span>, <span title="RMVB: Real Media Variable Bitrate">RMVB</span>, <span title="RPM: Real Media Plug-in Metafile">RPM</span>, RSRC, RTF, <span title="RV: Real Video">RV</span>, RW2, RWL, RWZ, SO, <span title="SR2: Sony RAW Format 2 (TIFF-like)">SR2</span>, <span title="SRF: Sony RAW Format (TIFF-like)">SRF</span>, SRW, SVG, <span title="SWF: Shockwave Flash">SWF</span>, <span title="THM: Canon Thumbnail (aka. JPG)">THM</span>, THMX, <span title="TIF: Tagged Image File Format (.3)">TIF</span>, <span title="TIFF: Tagged Image File Format (.4)">TIFF</span>, TTC, TTF, TUB, VOB, VRD, <span title="WAV: WAVeform (Windows digital audio format)">WAV</span>, <span title="WDP: Windows Media Photo (TIFF-based)">WDP</span>, <span title="WMA: Windows Media Audio (ASF-based)">WMA</span>, <span title="WMV: Windows Media Video (ASF-based)">WMV</span>, <span title="X3F: Sigma RAW format">X3F</span>, XHTML, XLA, XLAM, XLS, XLSB, XLSM, XLSX, XLT, XLTM, XLTX, <b style='font-size:120%'><span title="XMP: Extensible Metadata Platform data file">XMP</span></b>, and ZIP</span>.<hr/>
